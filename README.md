# 🛒 Shoprite Socket Communication System
This project demonstrates a **client-server application** built using **Python sockets**.  
It simulates a **Shoprite cashier system**, where the client sends product and cashier information to a server that validates, processes, and returns a formatted report.

## ⚙️ Features
✅ Client and server communication via TCP sockets  
✅ Input validation for cashier name, products, and prices  
✅ Report generation on the server side  
✅ Interactive terminal input for 5 products  
✅ Real-time communication between client and server  

## 🧠 Overview
- The **ShopriteClient** collects:
  - Cashier name  
  - Product names and prices  
- Sends this data to the **ShopriteServer** via socket connection.  
- The **ShopriteServer**:
  - Validates the received data  
  - Generates a transaction report  
  - Sends the formatted report back to the client.  

## 📁 Project Structure
│ Shoprite-Socket-Communication/
├── shoprite_client.py # Client program
├── shoprite_server.py # Server program
└── README.md # Project documentation

Welcome to Shoprite Program
Input your name: Tumi
Input five products
Product(1) name: Bread
Input price for Bread: 12.99
...
Data received and validated successfully
---------------Report--------------
Shoprite Report
Product Name   | Price

Cashier Name: Tumi
1. Bread----------R12.99
2. Milk-----------R20.50
...
-----------------------------------
Server listening on :8014
Connection from ('127.0.0.1', 52540)
Data received and validated successfully

⚡ Troubleshooting
If you get a “Port already in use” error:
Change the port in both files:
port = 8015
Then restart both scripts.
If the client hangs or doesn't connect:
Ensure the server is running before you start the client.

🧑‍💻 Author
South-Steez
💡 Python Networking & Automation Enthusiast
📍 GitHub: South-Steez
