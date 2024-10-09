"""
Jakub
date:30/9/24
task if classwork
"""
# #task1
# sName = str(input('Enter your name:')).capitalize()
# 
# if len(sName)<7:
#     print("Hello", sName ,', ur name is short')
# elif len(sName)<10:
#     print("Hello", sName ,', ur name is long')
# elif len(sName)>10:
#     print("Hello", sName ,', Your name is hella long')
#     
#task2

# print("1. Music \n  \n2. History\n  \n3. DEsign and Technology\n\n4. Exit")
# subject = int(input('Enter your option>'))
# 
# if subject == 1:
#     print('You chose Music')
# 
# 
# if subject == 2:
#     print('You chose History')
# 
# if subject == 3:
#     print('You chose DEsign and Technology')
# 
# if subject == 4:
#     print('Goodbye')
#     
# if subject>4:
#     print('invalid')
#     
# if subject<1:
#     print('invalid')

#task 3

# import random
# 
# roll = random.randint(1,6)
# roll2 = random.randint(1,6)
# 
# 
# if roll != roll2:
#     print('Your score is:',roll + roll2)
# 
# if roll == roll2:
#     print('Your score is doubled:',(roll + roll2)*2)

#task 4
# 
# price = int(input('Enter the amount that you will spend to see your discount:'))
# 
# if price >= 200:
#     print("You goods cost",price,"but at 10% discount you pay: $",(price/100*90))
#           
# elif price >= 100:
#     print("You goods cost",price,"but at 5% discount you pay: $",(price/100*95))
#     
# elif price < 100:
#     print('You pay',price,"as you get no discount, sorry:")
#     
#task 5

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# 
# 
# if num1 > num2:
#     difference = num1 - num2
#     
# else:
#     difference = num2 - num1
# 
# print("The difference is", difference)