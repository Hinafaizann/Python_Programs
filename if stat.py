age =int(input("Enter your age: "))
#print("Your age is: " + str(age))

if age>=6 and age<=80:
    if age<18:
        print("You cannot drive")

    elif age == 18:
        print("We will think about you")

else:
        print("Your age is either less than 6 or greater than 80, You can't drive ")