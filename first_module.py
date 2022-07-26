class Robot:
    """This is Roboat Class Here Show name and Age"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)


class Human(Robot):
    def __init__(self,name,age,food):
        super().__init__(name,age)
        self.food = food

    def show_food(self):
        print(self.food)


