class Student :
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    # instance method
    def show(self):
        print(self.name)
        print(self.roll)


stu1 = Student('shukumar', 1)
stu1.show()