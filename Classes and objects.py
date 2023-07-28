#Modules are any external files you gonna use in your program
#list of python modules :search on google and get every module according to your version of P
#PIP IS BASICALLY A PACKAGE MANAGER , see "site packages option here in lib folder to see the installed exteral files which you installed using pip
# Built-in modules , External modules

#Classes and Objects makes your program more organised and powerful

#For something in real world which python dont have data type then we can define our own data type by making CLASSES

from Student import Stu

Student1 =  Stu("Jim","CS", 3.1, False)
             #Student1 is the object being created , Stu is the class name

print(Student1.on_honor_roll()) #onhonorroll is the name of the function where the condition is applied

