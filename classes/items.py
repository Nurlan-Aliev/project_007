class Item:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def use(self):
        print(self.content)

    def look(self):
        print(self.content)

    def __str__(self):
        return self.name
