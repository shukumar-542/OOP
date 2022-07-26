class Doremon:
    def doremon_self(self):
        print('I am doermon and i am come from future')

    def gadget(self):
        print('new gadget')

class Nobita(Doremon):
    def nobita_self(self):
        print('I am Nobita and my hobby is sleeping')

class Shizuka(Nobita):
    def shizuka_self(self):
        print('my hobby is singing')


doremon = Doremon()
nobita = Nobita()
shizuka = Shizuka()

nobita.gadget()
shizuka.doremon_self()
