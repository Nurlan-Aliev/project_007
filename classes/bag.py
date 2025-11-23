class Bag:
    def __init__(self, *args):
        self.items = [item for item in args]

    def add(self, *args):
        for item in args:
            if len(self.items) > 5:
                print("Bag is full")
                return False
            self.items.append(item)
        return True

    def remove(self, item):
        self.items.remove(item)

    def is_in_bag(self, *args):
        for item in args:
            if item not in self.items:
                return False
        return True

    def __str__(self):
        return self.items

    def __iter__(self):
        return iter(self.items)

    def __bool__(self):
        return bool(self.items)
