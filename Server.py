
import socket
import re

class ShopriteServer:
    def __init__(self, host="", port=8014):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

    def validate_cashier_name(self, cashier_name):
        return len(cashier_name) > 0

    def validate_product_and_price_lists(self, products, prices):
        return len(products) > 0 and len(prices) > 0
    def generate_report(self, cashier_name, products, prices):
            # Implement the report generation logic here
        report = f"\n---------------Report--------------\nShoprite Report\nProduct Name   | Price\n\nCashier Name: {cashier_name}\n\n"
        for i, (product, price) in enumerate(zip(products, prices), start=1):
            report += f"{i}. {product}----------R{price}\n"
        report += "-----------------------------------\n"
        return report

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")

            # Receive cashier's name
            cashier_name = client_socket.recv(1024).decode()
            if not self.validate_cashier_name(cashier_name):
                client_socket.send("Invalid cashier name".encode())
                client_socket.close()
                continue

            # Receive products and prices
            products = client_socket.recv(1024).decode()
            prices = client_socket.recv(1024).decode()
            products_list = re.findall(r'\b\w+\b', products)
            prices_list = re.findall(r'\b\d+\.\d{2}\b', prices)

            # Validate product and price lists
            if not self.validate_product_and_price_lists(products_list, prices_list):
                client_socket.send("Invalid product or price list".encode())
                client_socket.close()
                continue

            # Send validated data back to client
            client_socket.send("Data received and validated successfully".encode())
            # Generate and send the report
            report = self.generate_report(cashier_name, products_list, prices_list)
            client_socket.send(report.encode())
            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    shoprite_server = ShopriteServer()
    shoprite_server.start()


