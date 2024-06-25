import os
class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self, amount):
        self.balance = self.balance+amount
        print(f"Your balance was increased by an amount {amount} CZK.")

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            answer= "yes"
            while answer == "yes":
                answer=input("Want you know your current balance? Write yes or no.\n")
                if answer =="no":
                    os.system("cls")
                    print("Thank you see you later")
                else:
                    self.balance=self.balance-30
                    print(f"Your balance is {self.balance} CZK.")
        else:
            print("Transaction declined")
            print("Do you want to take a loan?")
    
    def deposit(self,amount):
        self.balance= self.balance+amount
        print(f"An amount of {amount} CZK was deposited")
        answer= "yes"
        while answer == "yes":
            answer=input("Want you know your current balance? Write yes or no.\n")
            if answer =="no":
                os.system("cls")
                print("Thank you see you later")
            else:
                self.balance=self.balance-30
                print(f"Your balance is {self.balance} CZK.")

bankaccount=BankAccount("2000226448/2010", 55236.78)
bankaccount.withdraw(float(input("How much do you want to withdraw?\n")))
bankaccount.deposit(float(input("How much want you to deposit?\n")))