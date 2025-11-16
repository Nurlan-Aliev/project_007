class Bag:
    def __init__(self):
        self.items = []

    def add(self, new_item):
        self.items.append(new_item)

    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        return self.items

    def __iter__(self):
        return iter(self.items)
