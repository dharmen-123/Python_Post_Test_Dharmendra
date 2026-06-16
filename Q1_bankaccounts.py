# Q1. Create a class BankAccount with: (4 Marks)
# • Private variable __balance = 10000
# • Method deposit(amount) fi add to balance and print new balance
# • Method withdraw(amount) fi if amount > balance print 'Insufficient!', else deduct
# • Method get_balance() fi print current balance
# Create 2 objects and perform deposit and withdraw operations on both.

class BankAccount:
    __balance=10000

    def deposit(self, amount):
        self.__balance+=amount
        print("New balance-",self.__balance)

    def withdraw(self,amount):
        if(amount>self.__balance):
            print("Insufficient balance")
        else:
            self.__balance-=amount
            print("Amount withdraw successfully") 
    def get_balance(self):
        print("Total balance-",self.__balance)

B=BankAccount()
B.deposit(2000)
B.withdraw(5000)
B.get_balance()
print()
A=BankAccount()
B.deposit(3000)
B.withdraw(2000)
B.get_balance()
