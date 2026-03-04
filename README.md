🏦 Simple Bank Account Manager (Python)

A simple command-line bank account manager built in Python using Object-Oriented Programming (OOP).
This project simulates basic banking operations such as checking balance, depositing money, and withdrawing funds.

The goal of the project was to practice:

Python classes and inheritance

Input validation

Control flow with while loops

Basic program structure and separation of responsibilities

📌 Features

Create a client account with:

Name

Last name

Account number

Initial balance

Banking operations:

View account balance

Deposit money

Withdraw money (with insufficient funds protection)

Exit the program

Input validation for:

Names (letters and spaces only)

Account number (digits only)

Balance (numeric value)

🧠 Concepts Practiced

This project focuses on fundamental programming concepts:

Object-Oriented Programming

Class inheritance (Client inherits from Person)

Instance methods

Encapsulation of banking logic inside the class

Control Flow

while loops for menu navigation

Conditional logic (if / elif / else)

Input Validation

Checking user inputs

Handling numeric conversions with try/except

Code Organization

The program is structured into small functions responsible for one task:

Function	Responsibility
create_client()	Creates and returns a client object
option()	Displays and validates menu options
bank_account()	Main program loop
Validation functions	Validate user inputs
🏗 Project Structure
bank_account_manager.py
│
├── Person class
├── Client class
│
├── Input validation functions
│   ├── name_client()
│   ├── lastname_client()
│   ├── account_number_client()
│   └── balance_client()
│
├── create_client()
├── option()
└── bank_account()  (main program loop)
▶️ Example Interaction
Add your name: John
Add your lastname: Smith
Add your account number: 12345
Add your balance: 500

Choose an option:
1. balance
2. deposit
3. withdraw
4. out

> 2
Amount: 200

client: John Smith. account number: 12345. balance: 700
🚀 How to Run

Make sure Python is installed.

python bank_account_manager.py
📚 What I Learned

While building this project I improved my understanding of:

Structuring Python programs

Designing classes and methods

Separating logic into reusable functions

Handling user input safely

🔧 Possible Future Improvements

Support multiple bank accounts

Store account data in a file or database

Improve error handling

Add transaction history

Build a graphical interface (GUI)
