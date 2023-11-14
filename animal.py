# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
# конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля

class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.sound = sound
        self.species = species

    def make_sound(self):
        print(f'{self.species} {self.name} said {self.sound}')
    def move(self):
        print(f'{self.species} {self.name} moves')
    def swim(self):
        print(f"{self.species} {self.name} swim")

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger", "Tiger's sound")

    def swim(self):
        print(f"{self.species} {self.name} swim like tiger")

    

class Crocodile(Animal):
    def __init__(self, name):
        super().__init__(name, "Crocodile", "Croco sound")

    def swim(self):
        print(f"{self.species} {self.name} swim like croco")

class Kangoroo(Animal):
    def __init__(self, name):
        super().__init__(name, "Kangoroo", "Kangoroo's sound")

    def move(self):
        print(f'{self.species} {self.name} jump')

tiger = Tiger("momo")
crocodie = Crocodile("koki")
kangoroo = Kangoroo("poko")
crocodie.swim()
tiger.swim()
crocodie.make_sound()
kangoroo.move()