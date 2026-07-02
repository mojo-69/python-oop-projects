class BankAccount():
    def __init__(self):
        self.AccountNumber=int(input("Account Number :"))
        self.AccountHolder=input("\nAccount Holder : ")
        self.Balance=int(input("\nBalance :"))
        self.transaction=0
        self.history=[]
        self.pin=9855
    def display_details(self):
        print(f"\nAccount Number : {self.AccountNumber}")
        print(f"\n Account Holder : {self.AccountHolder}")
        print(f"\n Balance : {self.Balance}")
    def deposit(self):
        PIN=int(input("enter pin"))
        if PIN==self.pin:
            self.deposit=int(input("Enter Deposit Amount"))
            self.Balance=self.Balance+self.deposit
            self.transaction+=1
            self.history.append(f"Deposit : {self.deposit}")
            print(f"Balance : {self.Balance}")
        else:
            print("Incorrect Pin")
        print(f"Balance : {self.Balance}")
    
    def withdrawl(self):
        PIN=int(input("enter pin"))
        if PIN==self.pin:
            self.withdrawl=int(input("Enter withdrawl Amount"))
            if self.Balance >= self.withdrawl:
                self.Balance=self.Balance-self.withdrawl
                self.transaction+=1
                self.history.append(f"Withdraw : {self.withdrawl}")
                print(f"Balance : {self.Balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")
    def check_balance(self):
        print(f"balance: {self.Balance}")
    def transaction_count(self):
        print(f"Total Transaction : {self.transaction}")
    def change_account_holder(self):
        print(f"Old name:{self.AccountHolder}")
        self.NewAccountHolder=input("New Name")
        self.AccountHolder=self.NewAccountHolder
        print(f"Update Nmae: {self.AccountHolder}")
        print("Name Successfully change")
    def account_status(self):
        if self.Balance>=500000:
            print(f"{self.AccountHolder} have a Gold Account")
        elif self.Balance>=10000:
            print(f"{self.AccountHolder} have a Premium Account")
        else:
            print(f"{self.AccountHolder} have a Normal Account")
    def transaction_history(self):
        for i in self.history:
            print(i)
    def change_pin(self):
        
        self.Newpin=int(input("New Pin"))
        self.pin=self.Newpin
        
        print("Name Successfully change")
c1=BankAccount()
while True:
    print("1->display details")
    print("2-> Deposit")
    print("3-> withdrawl")
    print("4-> check balance")
    print("5-> transaction count")
    print("6-> change account holder")
    print("7 -> account status")
    print("8 -> Histroy")
    print("9-> Change pin")
    print("10-> exit")
    
    choice=int(input("Enter your choice"))
    if choice==1:
        c1.display_details()
    elif choice==2:
        c1.deposit()
    elif choice==3:
        c1.withdrawl()
    elif choice==4:
        c1.check_balance()
    elif choice==5:
        c1.transaction_count()
    elif choice==6:
        c1.change_account_holder()
    elif choice==7:
        c1.account_status()
    elif choice==8:
        c1.transaction_history()
    elif choice==9:
        c1.change_pin()
    elif choice==10:
        print("Thank You 😘")
        break
    
        
    
        
        
