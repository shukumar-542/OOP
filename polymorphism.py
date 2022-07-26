class Human:
    def __init__(self,name):
        self.name =  name
    def show_name(self):
        print(self.name)
class Robot:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
human = Human('shukumar')
robot = Robot('nobita')
for i in (human, robot):
    i.show_name()

a = 'shukumar'
b = 'ghosh'
c = a.__add__(b)
print(c)


class profile:
    def name(self,first=None,middle=None,last=None):
        if(first != None and middle != None  and last != None):
            print(first+" "+middle+ " "+last)
        elif (first != None and middle != None):
            print(first + " " + middle)
        else:
            print(first)
p = profile()
p.name( 'shukumar')