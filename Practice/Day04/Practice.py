#defin object and class
#Exercise 1
class Account :
     def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

     def deposit(self, amount):
        self.balance += amount

     def withdraw(self, amount):
        self.balance -= amount

     def statement(self):
        print(f"{self.owner}, {self.balance} ETB")

    #Exercise 2    
     def __init__(self, balance):
        self.__balance = balance  #private
     def get_balance(self):
        return self.__balance
     def withdraw(self, amount):
        if amount > self.__balance:
            print ("Insufficient funds")
            return
        self.__balance -= amount
    
    # using it
israel=Account(500)
israel.withdraw(900)
print(israel.get_balance())