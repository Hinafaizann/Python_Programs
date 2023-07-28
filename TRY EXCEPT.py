'''
MY
COMMENTS
'''
try:
    answer =10/0
    number= int(input("input a number pleasee:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid number")