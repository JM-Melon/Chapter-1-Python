"""
Jakub
date:4/9/24
task 6-8 HW
"""


pi = 3.14
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
totalLiquid = round(pi*r**2*h)
print("The volume of a cyliner is", totalLiquid)


earthWeight = float(input("Enter your weight: " ))
moonWeight = round((float(earthWeight / 100)* 16.5),2)
print (moonWeight)

gardenLenght = float(input("How long is thy garden in metres:"))
gardenWidth = float(input("How wide is thy garden in metres:"))
houseLenght = float(input("How long is thy house in metres:"))
houseWidth = float(input("How wide is thy house in metres:"))

gardenArea = gardenLenght * gardenWidth
houseArea = houseWidth * houseLenght

gardenArea2 = gardenArea - houseArea
print("Your garden is ", gardenArea2, "metres squared" )

time = round((gardenArea2/2/60),2)
print("It will take you",time, "minutes, to cut your lawn")



