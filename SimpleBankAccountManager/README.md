🏦 Bank Account Manager (Python OOP Project)

A simple command-line banking application built with Python and Object-Oriented Programming (OOP).
This project simulates a basic bank account system where users can create an account, check their balance, deposit money, and withdraw funds with validation rules.

The goal of this project was to strengthen my understanding of Python fundamentals, OOP design, and input validation.

🚀 Key Features

✔ Create a client account with validated input
✔ View current account balance
✔ Deposit funds into the account
✔ Withdraw funds with insufficient balance protection
✔ Menu-based interaction using a loop-driven CLI

🧠 Technical Concepts Demonstrated

This project focuses on core Python development skills:

Object-Oriented Programming

Class inheritance (Client inherits from Person)

Instance methods

Encapsulation of business logic inside classes

Program Design

Separation of responsibilities across functions

Clear control flow with a menu-driven loop

Reusable validation functions

Input Handling & Validation

Numeric validation

Name validation

Error handling for incorrect inputs

🏗 Architecture Overview
Person
  │
  └── Client
        ├── deposit()
        ├── withdraw()
        └── __str__()

Program Flow
  ├── create_client()
  ├── option()
  └── bank_account()  → main loop

The application separates responsibilities:

Component	Responsibility
Client class	Handles banking logic
Validation functions	Ensure correct user input
bank_account()	Manages the program flow
▶️ Example CLI Interaction
Add your name: Ana
Add your lastname: Lopez
Add your account number: 12345
Add your balance: 500

Choose an option:
1. balance
2. deposit
3. withdraw
4. out

> 2
Amount: 200

client: Ana Lopez. account number: 12345. balance: 700
🛠 Technologies Used

Python 3

Object-Oriented Programming

CLI (Command Line Interface)

💡 What This Project Demonstrates

This project highlights my ability to:

Design Python programs using clean structure

Implement OOP concepts

Write modular and readable code

Validate and manage user input safely