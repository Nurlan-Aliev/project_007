class Item:
    def __init__(self, name):
        self.name = name

    def use(self):
        pass

    def look(self):
        pass

    def __str__(self):
        return self.name


class Note(Item):
    def __init__(self, name, content):
        super().__init__(name)
        self.content = content

    def use(self):
        print(self.content)

    def look(self):
        print(self.content)