from datetime import datetime
import time

# Get the current date and time
date_time = datetime.now()
date = date_time.date()
current_time = date_time.strftime("%H:%M:%S")

class BankAccount:
    def __init__(self, owner, account_number, password, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been added to your account on {date}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, you are broke. Please make a deposit and try again.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
        
    @staticmethod
    def customer_care():
        print("Hello, this is customer care. How may I help you?")
        print("1. Call us")
        print("2. Chat with us")

# Dictionary to store bank accounts by account number
accounts = {
    "9035492056": BankAccount("Vortex", "9035492056", "Dinhofundz", 1000),
    "8706298906": BankAccount("Diamond", "8706298906", "Adigunme", 500)
}


def login():
    """Function to handle user login by account number and password."""
    account_number = input("Enter your account number: ").strip()
    password = input("Enter your password: ").strip()

    # Check if the account exists and password matches
    if account_number in accounts and accounts[account_number].password == password:
        print("Login successful!")
        time.sleep(1)
        print("Welcome to Diamond Banking System")
        time.sleep(1)
        print("Hello, how can we help you today?")
        time.sleep(1)
        return accounts[account_number]
    else:
        print("Invalid account number or password. Please try again.")
        return None

def main():
    account = None
    while not account:
        account = login()

    while True:
        # Display menu
        print(f"\n{account.owner}'s Bank Account")
        print("1. Make a deposit")
        print("2. Withdraw")
        print("3. Check your balance")
        print("4. Customer Care")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")
        
        # Perform actions based on user choice
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            BankAccount.customer_care()
            float(input("Enter the number of what i can help you with: "))
        elif choice == '5':
            print("Thank you for using the bank account service.")
            break
        else:
            print("Invalid choice, please select a valid number.")

# Start the main function
main()



