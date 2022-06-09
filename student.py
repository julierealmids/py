from curses import ALL_MOUSE_EVENTS


class Account:
    
    def __init__(self,acc_number,acc_name):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be less than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            print(self.deposits)
            return f"Hello,you have deposited {amount} and your new balance is {self.balance}"
               
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance is {amount}, you cannot withdraw the {self.balance}"
        elif amount <0:
            return f"You cannot withdraw a negative amount"
        else:
            self.balance-=amount
            self.withdrawals.append(self.balance)
            print(self.withdrawals)
            return f"You have withdrawn {amount},your balance is {self.balance}"
        
    def deposits_statement(self):
        print(self.deposits,sep="/n")
        
    def withdrawals_statement(self):
        print(*self.withdrawals,sep="/n")