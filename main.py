# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("    / |")
print("   /  |")
print("  /   |")
print(" /____|")

#Variablessssssssss
character_name = "Hina"
character_age= "24"
print("Her \"name\" is " + character_name + "," )
print("Her \"age\" is: \n" + character_age + ".")

#Python functionsssssssss

character_name = "Nida khalid"
character_age= "25"
#Concatenation is done by + symbol
print( character_name + " was " + character_age + " years old")
print("Her \"age\" is now: " + character_age + ".")
print(character_name.lower())
print(character_name.islower()) #will resturn false
print(character_name.lower().islower())
print(len(character_name))
print(character_name [0])
print(character_name.index("id")) #it will return the index where is id in nida
print(character_name.replace("khalid", "Zain"))




#Working with numbersssssssss
print ("Working with numbersss :")
print (3 *(2 +5)  )
# We have to convert numbers into string in order to print numbers and string in a single print function otherwise no concatenation can do exist
my_num = 10
print(str(my_num) + " is my fav number")
my_num = -10
print(str(abs(my_num)) +" favvv" )
print (pow(3, 7))
print (max(3, 7))
print (round(6.70))
from math import *
now_num = 3.7
print (floor (now_num)) #3
print (ceil (4.2)) #5
print(sqrt(now_num))



#Taking input from userrrr
#name= input("Enter your name:")
#age= input("Enter your age:")
#print("Hello " + name + "! you are: " + age )





##Mad lib gamessssss
##print("Roses are red")
#color =input("Enter a color: ")
# plural_noun =input("Enter a plural Nouns: ")
# celebrity = input("Enter a celebirty name:")
# print("Roses are: " + color)
# print(plural_noun + " are blue")
# print("I love celebrity" +celebrity)



##Dealing with listsssssssss :when we have alot of data and we have to manage and organise it
friends = [ "Nida", "Farii", "Ateeqa" , "Izza"] ##Can store numbers in a list too.
##print(friends)
print(friends[-3])
##print(friends[1:]) #1 and after all of the 1s will be printed
print(friends[2:3]) ##Will not print 3
## Modify the elements in list
friends[1] = "My farii"
print(friends[1])

##List Functionsssssssssss :get info from lists and modify lists
lucky_numbers= [4, 3, 5 , 8, 9, 10]
friends = [ "Nida", "Farii", "Ateeqa" , "Izza"]

print(friends)