# Date: Sept 2024
# Author: Jakub Malecki
# Purpose: Hw task 2-5


#task 2
#print(pagram [:] would display the whole phrase index 0 - 43

#task 3
# it would not worka as its out of range as there is no index 4 in "Mary"
#you cannot change the value of a string after it is determined

#task 4
#i beleive the first one will work and display all 4 words
word1 = "Leaving"
word2 = "Cert"
word3 = "Computer"
word4 = "Science"

subjectName = word1 + word2 + word3 + word4
print(subjectName)
#no spaces id add a comma to each word


#i beleive that it will return the first 3 indexes and the  16th index onwards
pangram = "The quick brown fox jumps over the lazy dogs!"
print(pangram[:3] + pangram[16:])
# no space on the second word id change the 3 to a 4


#it will conjugate a noun into its plural states

noun = input("Enter a singular noun:")
print("The plural of ",noun," is ",noun,"s")
#u can use commas instead of the plusses


#task 5
# 1= d
# 2= 0123456789
# 3= Z0123456789
# 4= ABCDEFGHIJKLMONPWRSTUWXYZ0
# 5= abcdefghijklmnopqrstuvwxyz
# 6= b
# 7= f
# 8=ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 9= A
