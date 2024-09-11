"""
Jakub Malecki
date 24/sep
classwork tasks 1-10
"""

#program to average five randomly genereated numbvers
import random

low = random.randint(1,100)
high = random.randint(low,100)

#generste the 5 random numbers between low and high
n1 = random.randint(low, high)
n2 = random.randint(low, high)
n3 = random.randint(low, high)
n4 = random.randint(low, high)
n5 = random.randint(low, high)

#compute their average
average = (n1+n2+n3+n4+n5)/5

#add the 5 numbers and display the result
print("The average of", n1, n2, n3, n4, n5, "is", average)