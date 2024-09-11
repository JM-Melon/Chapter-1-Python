"""
Jakub Malecki
date 24/sep
classwork tasks 1-10
"""

#Program to multiply 2 randomly generated numbers
import random

num1 = random.randint(1,10)# generate a number between 1-10
num2 = random.randint(1,10)# generate a number between 1-10

#multiply the 2 numbers and display the result
print(num1, "times", num2, "=", num1*num2)