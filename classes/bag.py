class Bag:
    def __init__(self):
        self.items = []

    def add(self, *args):
        for item in args:
            if len(self.items) > 5:
                print('Bag is full')
                return False
            self.items.append(item)
        return True

    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        return self.items

    def __iter__(self):
        return iter(self.items)
