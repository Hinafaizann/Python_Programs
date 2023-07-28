class Stu:
    def __init__(self,  name, major, gpa, is_on_probation): #init is initialization function of student
        self.name = name #self.name is going to be the "name" of the student which student will enter
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa>=3.5: #self.gpa is the reference to the parameter gpa which will actually be entered by user
            return True
        else:
            return False


