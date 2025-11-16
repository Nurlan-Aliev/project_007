from classes.bag import Bag


class Hero:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()
        self.visible = True

    def __str__(self):
        return self.name


class Gryffindor(Hero):
    def __int__(self, name):
        super().__init__(name)
        self.house = "Gryffindor"


class Slytherin(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.house = "Slytherin"


class Ravenclaw(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.house = "Ravenclaw"


class Hufflepuff(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.house = "Hufflepuff"
