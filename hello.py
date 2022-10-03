class BankAccount:

    def __init__(self, balance: int = 0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,value):
        self.__balance = value

    def deposit(self, amount): 
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance


