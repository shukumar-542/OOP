class Cartoon:
    """this my first class
    and this is my first using doc class"""
    series = 'tv series' #class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)

obj1 = Cartoon("doremon", 10)
obj2 = Cartoon("sinchan",20)

print(Cartoon.__doc__)

obj1.show()
obj2.show()
