import os
class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self, amount):
        self.balance = self.balance+amount
        print(f"Your balance was increased by an amount {amount} CZK.")

    def withdraw(self,amount):
        if self.balance>amount+30:
            self.balance=int((self.balance-amount)*100)/100
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
            answer="yes"
            input("Transaction declined\nDo you want to take a loan?\n")
            if answer=="yes":
                remain=amount-self.balance+300
                
                print(f"Your balance was increased by {remain-300} CZK, RPNS is 18%.")
                self.balance=int((self.balance-amount+remain)*100)/100
                print("Now you take your money.")
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
                os.system("cls") 
                print("Thank you, good bye")
                
    
    def deposit(self,amount):
        self.balance= int((self.balance+amount)*100)/100
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
withdrawal=float(input("How much do you want to withdraw?\n"))
bankaccount.withdraw(withdrawal)
bankaccount.deposit(float(input("How much want you to deposit?\n")))