# Q2. Create a Bank account with members account number, name, type of account, and balance. Write constructor and methods to deposit and withdraw.


class BankAccount:
    def __init__(self, accno, name, acctype, balance=0):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount, "| New Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount, "| Remaining Balance:", self.balance)


# Input from user
accno = int(input("Enter Account Number: "))
name = input("Enter Name: ")
acctype = input("Enter Account Type (Savings/Current): ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(accno, name, acctype, balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif ch == 2:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif ch == 3:
        break
    else:
        print("Invalid choice!")

