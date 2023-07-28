##List Functionsssssssssss :get info from lists and modify lists
lucky_numbers= [4, 3, 5 , 8, 9, 10]
friends = [ [('a', 'DT'), ('spokenswomen', 'NN')], "(nida, farii)", "Nida", "Farii", "Ateeqa" , "Izza"]
##to append two lists :use EXTEND function
##to append an element in a list use APPEND function
##friends.append("My izzu")
##friends.extend(lucky_numbers)
friends.insert(2, "kim") ##insert at 2 posistion and all others will be pushed next
friends.remove("Izza") ##remove element , use Clear function to clear a list
friends.pop() ##removes last element
print (friends.index("kim")) #to find some element in list
print (friends.count("kim")) ##how many times an element came
#friends.sort() #sorting listtt #use reverse to reverse list
friends2= friends.copy() ##copy a list
print(friends2)
print(friends)
print("printing friend at oth index: ")
print(friends[0])

print("printing friend at 1th index: ")
print(friends[1])

print("printing friend at 2th index: ")
print(friends[2])

##Tuplessss in python :structure where we can store info just like list but have differences
coordinates = (4,5) ## tuples is immutable they cant be changed or modfied , ##now we have tuple having two coorinates
coordinates2= [(2, 3), (4, 5)] ##a list of tuples
print(coordinates[-2])
print(coordinates2[-1])


