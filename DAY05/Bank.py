'''
Name : Tejal Dadaji Pagar
Cohort : AIML & TEP cohort 2026
Day : Thursday
Date : 13/08/2026
Description : MiniProject
'''
class BankAccount:
    def __init__(self,owner,balance):
        self.owner =owner
        self.balance =balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance :
            self.balance -= amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"Balance is :{self.balance}" )
account =BankAccount('Tejal',5000)
account.deposit(1500)
account.withdraw(1000)
account.show_balance()
