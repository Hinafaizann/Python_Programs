#Allows program to response #simple two boolean variablesssssss
is_male= False
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not male but you are tall")
else:
    print("you are neither male or tall")