#print(2**3)
def raise_to_power(base_num, pow_num):
    result=1
    for i in range(pow_num): #ranges between the number of times the pownum is, if pownum is 3 it will run 2 times
        result = result * base_num #2, 4, 8 #3, 9 , 27
    return result

print(raise_to_power(2,3 ))