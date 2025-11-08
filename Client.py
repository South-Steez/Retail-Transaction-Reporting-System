import socket
# Define the client class for Shoprite
class ShopriteClient:
    def __init__(self, host="", port=8014):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Try to bind the socket to the host and port
        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))
# Function to get the cashier's name
    def get_cashier_name(self):
        print("Welcome to Shoprite Program")
        return input("Input your name: ")
# Function to get the products and their prices
    def get_products_and_prices(self):
        products = []
        prices = []

        print("---------Product List------------")
        print("\nInput five products")
 # Loop to get the name and price of each product
        for i in range(5):
            product = input(f"Product({i + 1}) name: ")
            price = input(f"Input price for {product}: ")

            products.append(product)
            prices.append(price)

        print("---------------------------------")
        print("\nProducts added")
        print("\nPrices added")
        print(products)
        print(prices)

        return products, prices
  # Function to send data to the server
    def send_data_to_server(self, cashier_name, products, prices):
        self.client_socket.send(cashier_name.encode())
        self.client_socket.send(' '.join(products).encode())
        self.client_socket.send(' '.join(prices).encode())
  # Function to receive data from the server
    def receive_data_from_server(self):
        response = self.client_socket.recv(1024).decode()
        print(response)
   # Function to close the connection
    def close_connection(self):
        self.client_socket.close()
# Main function to run the client
if __name__ == "__main__":
    shoprite_client = ShopriteClient()

    cashier_name = shoprite_client.get_cashier_name()
    products, prices = shoprite_client.get_products_and_prices()

    shoprite_client.send_data_to_server(cashier_name, products, prices)
    shoprite_client.receive_data_from_server()

    shoprite_client.close_connection()
