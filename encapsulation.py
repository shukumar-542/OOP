class Nobit:
    def __init__(self):
        self.book = "comics"
        self.no = 10
        self._no = 20
        self.__no = 30
    def show(self):
        print(self.no)

class Shino(Nobit):
    def show_nobita(self):
        print("sino", self._Nobit__no)

class Shizuka(Nobit):
    def show_nobita(self):
        print('shizuka',self.no)

nobita =Nobit()
shino = Shino()
shizuka = Shizuka()

nobita.no = 15

nobita.show()
shino.show_nobita()
shizuka.show_nobita()
