from  abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def go_to_school(self):
        pass
class Child(Father):
    def go_to_school(self):
        print('yes')
    def playing(self):
        print('playing ')
    def singing(self):
        print('singing')

child = Child()
child.playing()
child.go_to_school()