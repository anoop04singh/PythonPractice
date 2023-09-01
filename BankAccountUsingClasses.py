##We Declare variable with Account Class having an owener name and initial Balance.
##Then we can use various function of account class to manange account Deposists and Withdrawals.
##If the Withdrawal amount is greater than the balance then the transaction is not processed and an error is shown.
class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep):
        self.dep = dep
        self.balance = self.dep + self.balance
        return "Your Deposit is {} and updated balance is {}".format(self.dep,self.balance)
    def withdraw(self,withd):
        self.withd  = withd
        if self.withd > self.balance:
            return "YOU DON'T HAVE ENOUGH BALANCE"
        else:
            self.balance = self.balance - self.withd
            return "Your Withdrawal is {} and updated balance is {}".format(self.withd,self.balance)
