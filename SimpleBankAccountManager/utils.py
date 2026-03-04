class Person:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Client(Person):

    def __init__(self, name, lastname, account_number, balance):
        super().__init__(name, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return  f"client: {self.name} {self.lastname}. account number: {self.account_number}. balance: {self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit cannot be negative")
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return False

        if amount > self.balance:
            print("Insufficient funds")
            return False

        self.balance -= amount
        return True

def name_client():
     while True:
         name = input("Add your name ").title().strip()

         if name.replace(" ", "").isalpha():
             return name

         print("Only letters and spaces are allowed")

def lastname_client():
     while True:
         lastname = input("Add your lastname ").strip()

         if lastname.replace(" ", "").isalpha():
             return lastname

         print("Only letters and spaces are allowed")

def account_number_client():
    while True:
        account_number = input("Add your account number ").strip()

        if account_number.isdigit():
            return account_number

        print("Only digits are allowed")

def balance_client():
    while True:
        balance = input("Add your balance: ").strip()

        try:
            return float(balance)
        except ValueError:
            print("invalid balance")
            continue

def create_client():
    name = name_client()
    last_name = lastname_client()
    account_number = account_number_client()
    balance = balance_client()

    client = Client(name, last_name, account_number, balance)

    return client

def option():
    options = ['1. balance', '2. deposit', '3. withdraw', '4. out']
    while True:
        choice = input(f"Choose an option: {options} ").strip()
        if choice.isdigit():
            choice = int(choice)
        if choice in range(1, 5):
            return choice
        else:
            print("Invalid choice")
            continue

def bank_account():
    client = create_client()

    while True:
        choice = option()
        if choice == 1:
                print(client)

        elif choice == 2:
            amount = input("Amount: ").strip()
            if amount.isdigit():
                amount = int(amount)
                client.deposit(amount)
                print(client)
            else:
                print("Invalid amount")

        elif choice == 3:
            amount = input("Amount: ").strip()
            if amount.isdigit():
                amount = int(amount)
                client.withdraw(amount)
                print(client)
            else:
                print("Invalid amount")
        else:
            print("Hasta pronto :)")
            break



