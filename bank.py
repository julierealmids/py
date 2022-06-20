from datetime import datetime

class Account:
    acc_num=0
    acc_name=""
    deposits=[]
    withdrawals=[]
    def __init__(self,acc_num,acc_name):
        self.acc_num=acc_num
        self.acc_name=acc_name
        self.loan_balance=0
    def make_deposit(self,amount):
        self.deposits.append({
                              "date":datetime.now(),
                              "amount":amount,
                              "narration":"deposit"
                            })
        
        print(f"Hello {self.acc_name}, you have deposited {amount} and your balance is {self.get_balance()}")
    def make_withdrawals(self,withdrawal_amount):
        transaction=100
        withdrawal=transaction+withdrawal_amount
        if self.get_balance()-withdrawal>=0:
            self.withdrawals.append({
                              "date":datetime.now(),
                              "amount":withdrawal,
                              "narration":"withdrawal"
                            })
            print(f"Hello {self.acc_name}, you have withdrawn {withdrawal_amount} and your balance is {self.get_balance()}")
        else:
            print(f"Insufficient amount")
    def get_balance(self):
        total_deposits=0
        total_withdrawals=0
        for y in self.deposits:
            amount=y["amount"]
            total_deposits+=amount
        for z in self.withdrawals:
            amount=z["amount"]
            total_withdrawals+=amount
        balance=total_deposits-total_withdrawals
        return balance
    def get_deposits(self):
        for i in self.deposits:
            print(f"{i['narration']} {i['amount']} at {i['date']}")
    def get_withdrawals(self):
        for x in self.withdrawals:
            print(f"{x['narration']} {x['amount']} at {x['date']}")
    def current_balance(self):
        current_balance=self.balance
        return f"your current balance is{current_balance}"
    
    def get_fullstatement(self):
        full=self.deposits+self.withdrawals
        full = sorted(full, key=lambda d: d['date']) 
        for j in full:
            print(f"{j['date'].strftime('%d/%m/%y')}-{j['narration']}-{j['amount']}")
    def borrow_method(self,amount):
        sum=0
        for g in self.deposits:
            sum+=g["amount"]
        if (len(self.deposits))<10:
            print(f"Dear customer {self.acc_name} {self.acc_num} is ineligible to borrow a loan")
        elif (self.loan_amount)<100:
            print(f"Sorry you cannot borrow less than 100 to {self.acc_name} account number{self.acc_num}")
        elif amount>(sum//3):
            return f"Dear customer {self.acc_name} number {self.acc_num} is ineligible to borrow a loan"
        elif self.balance==0:
            print(f"Dear customer you cannot request a loan to account{'self.acc_num'}")
        elif self.loan_balance==0:
            print(f"Dear customer you are eligible to borrow a loan")
        def loan_repayment(self,amount):
            if amount<0:
                return f"Amount is invald"
        if amount > self. loan_balance:
            self.balance += amount-self.loan_balance
            return f"Dear {self.name} thank you for repaying your load of {amount-self.loan_balance} and your account  balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"
    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.balance += amount
            return










            
            
            
        
            
        
# Julliet=Account(acc_name="Nakayiza",acc_num=134256)
# print(f"Your account name is {Julliet.acc_name} with account number {Julliet.acc_num}")
# Julliet.make_deposit(5000)
# Julliet.make_deposit(10000)
# Julliet.make_withdrawals(3000)
# Julliet.make_withdrawals(12000)
# Julliet.make_deposit(20000)
# Julliet.make_withdrawals(10000)
# Julliet.get_deposits()
# Julliet.get_withdrawals()
# Julliet.get_fullstatement()
# Julliet.borrow_method(4000)

# date=datetime.now().strftime("%d/%m/%y")
# print(date)
