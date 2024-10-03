"""
Jakub
date:30/9/24
task oneNote boolion
"""

#1 and 0
#0 or 0
#1 and 0
#0 or 1
#0 and 1

import random

number = random.randint(1,10)

guess = int(input("Enter a number between 1 and 10: "))

if guess == number:
    print("Your guess was correct")
    print("Well done!")
    
# elif guess == number:
#     print("Your guess was wrong")
#     
print("Goodbye")