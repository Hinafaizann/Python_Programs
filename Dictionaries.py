#Special structure in python that allows us to store information in key-value pairs, a word/key is identifies and value is the information of that key/word
##Creating a dictionaryyyy
'''
monthConversions = {
    "Jan" : "January", #Jan is must be the unique key and January is the value
     1 : "February",
    "Mar" : "March",
    "Apr" : "April",
}
#print(monthConversions["Mar"]) ##1 way
#print(monthConversions.get(1, "Not a valid key" )) #get the value of 1, if 1 is not present then print not a valid key
#print(monthConversions[1 ])
print(monthConversions.keys()) #keys, values, items
'''
mydic = {
    "Set" : "well defined set of words",
    "mutable" :"changable, list",
    "immutable": "cant be changed, tuple",
    "cs": "Computer science"
}
print(mydic["Set"])