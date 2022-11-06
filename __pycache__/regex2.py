import re
import turtle


class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
        

obj = Calculator() 
a = int(input("First num?"))
b = int(input("Second num?"))
param = int(input("add, subs, mult or divide?")) 
if param == 1:
    print(obj.add(a, b))
if param == 2:
    print(obj.subtract(a, b))
if param == 3:
    print(obj.multiply(a, b))
if param == 4:
    print(obj.divide1(a, b))
