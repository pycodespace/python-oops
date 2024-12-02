class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount
        # write code here        

    def deposit(self, amount):
        # write code here
        self.balance += amount        

    def getBalance(self):
        # write code here
        return self.balance        


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        # write code here
        return self.balance * self.interestRate / 100  


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
demo1.deposit(500)
print(demo1.getBalance())        
        
 