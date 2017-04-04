#Real world problem taking advantage of OOP


""" Banking """
class BankAccount(object):  #Common properties of bank accounts in BankAccount class
    def __init__(self,owner_name,owner_id,balance,account_type):
        self.__security_number = 0  #Encapsulation
        self.credit_score = 10
        self.owner_name=owner_name
        self.owner_id=owner_id
        self.balance=balance
        self.account_type=account_type
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount


    def withdraw(self,amount):
        if amount>0 and amount<self.balance:
            self.balance-=amount

class PremiumBankAccount(BankAccount):  # Inheritance:: PremiumBankAccount inherits from parent BankAccount
    def __init__(self):
        self.__business_loan=0  # Encapsulation


    def apply_loan(self,amount):
        if amount>50000:
            self.__business_loan+=amount
            self.__business_loan=self.__business_loan+(amount*0.12*6)
            return 'You have been granted a loan of %0.2f. Debt balance %0.2f to be repaid in 6 months'%(amount,self.__business_loan)
        else: return 'Invaid loan amount!'


class StandardBankAccount(BankAccount):  # Inheritance:: StandardBankAccount inherits from parent BankAccount
    def __init__(self):
        self.__small_loan=0  # Encapsulation


    def apply_loan(self,amount):
        if amount > 50000 and self.__small_loan==0:
            self.__small_loan += amount
            self.__small_loan=self.__small_loan+(amount*0.12*6)
            return 'You have been granted a loan of %0.2f. Debt balance %0.2f to be repaid in 6 months' % (amount,self.__small_loan)
        else:
            return 'Invaid loan amount!'

def apply_loan(account_type,amount):          # Polymorphism demo
    return account_type.apply_loan(amount)