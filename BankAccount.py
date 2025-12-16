# Program to define a BankAccount class
class BankAccount:
    # Constructor to initialize account details
    def __init__(self, acc_number, name, balance=0.0):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

    # Method to display account information
    def display_info(self):
        print("\n--- Account Information ---")
        print(f"Account Number : {self.acc_number}")
        print(f"Account Holder : {self.name}")
        print(f"Current Balance: ₹{self.balance}")


# --- Example Usage ---
# Creating a BankAccount object
account1 = BankAccount(1001, "Utkarsh Mishra", 5000)

# Performing operations
account1.display_info()
account1.deposit(2000)
account1.withdraw(1500)
account1.display_info()
