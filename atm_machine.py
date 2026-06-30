class ATM:
    def __init__(self):
        self.account_holder = input("Enter Account Holder Name: ")
        self.account_number = int(input("Enter Account Number: "))
        self.balance = int(input("Enter Initial Balance: "))

    def display_details(self):
        print("\n===== Account Details =====")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance         : {self.balance}")

    def deposit(self):
        amount = int(input("Enter Deposit Amount: "))
        self.balance += amount
        print("Deposit Successful!")
        print(f"Current Balance : {self.balance}")

    def withdraw(self):
        amount = int(input("Enter Withdrawal Amount: "))

        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawal Successful!")
            print(f"Current Balance : {self.balance}")

    def check_balance(self):
        print(f"\nCurrent Balance : {self.balance}")



c1 = ATM()

while True:
    
    print("1. Display Details")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        c1.display_details()

    elif choice == "2":
        c1.deposit()

    elif choice == "3":
        c1.withdraw()

    elif choice == "4":
        c1.check_balance()

    elif choice == "5":
        print("Thank You! Visit Again.")
        break

    else:
        print("Invalid Choice!")
