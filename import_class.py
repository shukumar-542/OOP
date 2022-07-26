from first_module import  Robot
from  first_module import Human
from second_modeule import Animal

robot = Robot('sophiya','6year')
human = Human('shukumar','26year','rice')
animal = Animal('Tiger',"25Year","bear","pet animal")


robot.show_name()
robot.show_age()

human.show_name()
human.show_age()
human.show_food()

print("_"*5, "Animal" , "_"*5)
animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()