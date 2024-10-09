"""
Jakub
date:30/9/24
task HW  boolion
"""
#task 1

# 
# num1 = int(input ("Enter a Number:"))
# num2 = int(input ("Enter another Number:"))
# 
# num3 = num1%num2
# 
# if num3 != 0:
#     print("Those dont divide evenly")
#     
# else:
#     print("gj they do divide evenly")
#     
    
# #task 2

# 
# age = int(input("Enter age please:"))
# if age < 17:
#     print ("you are not able to apply, sorry")
# elif age >=17:
#     print("you can appply for driving test")
# 
# #task 3
# 
# price = int(input('Enter the total cost of your item:'))#this makes the person enter acost of thier product
# 
# if price >10000:
#     print('Please visit our tender in his office')# if the num is more than 10k it returns the quote
# # elif price <=10000:
# #     input('Enter quotes from 3 seperate suppliers:')
# #     input('Enter quotes from 3 seperate suppliers:') # uselesss as it just causes errors
# #     input('Enter quotes from 3 seperate suppliers:')
# elif price >= 500:
#     input('Enter quotes from 3 seperate suppliers:')
#     input('Enter quotes from 3 seperate suppliers:')# if the num is more or equal to 500 it returns quote
#     input('Enter quotes from 3 seperate suppliers:')  
# elif price < 500:
#     print('preoceed at the cash desk') #if the num is less then 500 it returns quote
#         
# #task 4 

ticket = input('Pick Option A , B , C: ').upper()#assigns ticket to the player input

if ticket == 'A':
    print('Youve won a trip to Dundrum shopping centre')#if player types 'A' they win such prize
elif ticket == 'B':
    print('Youve won a free trip to Tallaght')#if player types 'B' they win such prize
elif ticket == 'C':
    print('youve won a free trip to Broombridge')#if player types 'C' they win such prize
else:
    print('Invalid Entry')#if player types anything else they win such prize

#task 5 

grade = int(input('Enter your result:'))#student enters result

if grade>100:
    print('Not valid score')#if grade is higher than 100 it doesnt work
elif grade >= 90:
    print('h1')#h1 if between 90-100
elif grade >= 80:
    print('h2')#h2 if between 80-89
elif grade >= 70:
    print('h3')#h3 if between 70-79
elif grade >= 60:
    print('h4')#h4 if between 60-69
elif grade >= 50:
    print('h5')
elif grade >= 40:
    print('h6')
elif grade >= 30:
    print('h7')
elif grade >= 0:
    print('h8')
    

elif grade<0:
    print('Not valid score')#not valid score cuz result cant be below 0
