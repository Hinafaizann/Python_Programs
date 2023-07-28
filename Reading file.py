'''
r mode
w mode
a mode :append at the end but not updating existing
r+ mode :reading plus writing

'''
E_file =open("TEST AUTO tagged File CHECKED.txt", "r")
print(E_file.readable())
#print(E_file.readlines()) #
'''
reaadlines will convert the file into array 
and now we can access specific line by just pointing out its index
print(E_file.readlines()[1])
'''
E_file.close()