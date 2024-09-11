"""
Jakub Malecki
date 24/sep
classwork tasks 1-10
"""

# Ask the user for the principle
principal = input("Enter principal: ")
principal = float(principal)

#Ask the user for the interest rate
rate = input ("Enter rate:")
rate = float(rate)

#Ask the user for the length of time
time = input("Enter time in years: ")
time = float(time)

#Simple interest calculation
amount = principal * rate * time

#display the answer
print("The interest amount is ", amount)