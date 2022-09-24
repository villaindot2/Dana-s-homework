from __future__ import print_function
import math
from re import A


#Solve Problems using loops
#1) Write a program in Python to display the cube of the number upto given an integer. Go to the editor

# num = int(input('print number: '))
# print(f"Cube of namber {num} is {num**3}")

#2) Print list in reverse order using a loop

# array = []
# num = int(input())
# for i in range(num):
#     array.append(int(input()))
# print(f"First array: {array}.")
# print("Reverse array:[", end='')
# for i in reversed(array):
#     print(i,end=' ')
# print("]")

#3) Find the factorial of a given number

# num = int(input('Give me a number: '))
# print(f"Factorial = {math.factorial(num)}")

#4) Calculate the sum of all numbers from 1 to a given number

# num = int(input())
# a = 0
# for i in range(num+1):
#      a=i+a
# print(a)

#5) Given an integer x, return true if x is palindrome integer.

#Solve Problems using nested loops
#1) Write a program to use for loop to print the following reverse number pattern
# num = int(input())
# for i in range(num,0,-1): 
#     for j in range(i, 0, -1):
#         print(j, end=' ') 
#     print("")
#2) Write a program to use for loop to print the following number pattern
# num = int(input())
# for i in range(1, num + 1):
#         a = str(i)
#         print(a * i)
#         print(" ")

#Solve problems using regular or lambda functions
#1) Create a lambda function get_discount that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
# print('Введите цену')
# cost = int(input())
# print('Введите скидку')
# disc = int(input())
# get_discount = lambda cost, disc: cost*(disc/100)
# print(get_discount(cost,disc))

#2) Write a function sum_numbers that finds the sum of the first n natural numbers. Make your function recursive

#3)Create a function is_triplet that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.
#  is_triplet = lambda a,b,c: a**2 + b**2 == c**2

# if a>b and a>c:
#     print(is_triplet(b,c,a))
# if b>a and b>c:
#     print(is_triplet(a,c,b))
# if c>a and c>b:
#     print(is_triplet(a,b,c))
   

 

