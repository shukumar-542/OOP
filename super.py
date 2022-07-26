class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


class Human:
    def __init__(self,name,age,food):
        self.name = name
        self.age = age
        self.food = food

    def show_name(self):
         print(self.name)

    def show_age(self):
         print(self.age)

    def show_food(self):
        print(self.food)


class Animal(Robot,Human):
    def __init__(self,name, age,food,pet):
        Human.__init__(self,name, age,food)
        self.pet = pet

    def show_pet(self):
        print(self.pet)




robot = Robot('shopiya', '6year')
human = Human('shukumar','26year','rice')
animal = Animal('tiger','25','meet','pet animal')

print("_"*5 ,"Robot" ,"_"*5)
robot.show_name()
robot.show_age()

print("_"*5 , 'Human' ,"_"*5)
human.show_name()
human.show_age()
human.show_food()

print( '_'*5 , "animal" , "_"*5)
animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()