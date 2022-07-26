class Human:
    def __init__(self,name):
        self.name = name
    def show_info(self):
        print(self.name)
        print("Human Class")
    class Robot:
        def __init__(self, name):
            self.name = name
        def show_name(self):
            print(self.name)

        class Car:
            def __init__(self, name):
                self.name = name

            def show_car(self):
                print(self.name)



human = Human('shukumar')
robot =human.Robot("shophiya")
car = human.Robot.Car("scorpiyo")

human.show_info()
robot.show_name()
car.show_car()