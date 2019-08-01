class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        print("Added {} to account".format(deposit_amount))
        self.balance += deposit_amount

    def withdraw(self,withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return "Owner is: {} balance is {}".format(self.owner, self.balance)


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.balance)
print(acct1.owner)
acct1.deposit(50)
print (acct1.balance)

acct1.withdraw(100)
print (acct1.balance)
acct1.withdraw(500)
print(acct1)