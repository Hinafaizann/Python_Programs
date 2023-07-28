from Inheritence import classChef
class classChineseChef(classChef): #inheriting the classChef, so classChef is parent class

    def make_special(self):
        print("Makes chinesepulao")

MychineseChef = classChineseChef()
MychineseChef.make_special()