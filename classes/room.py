from classes.bag import Bag


class Room:
    def __init__(self, name, description, creature=None):
        self.name = name
        self.description = description
        self.creature = creature
        self.next_rooms = {}
        self.items = Bag()

    def add_room(self, *args):
        for room in args:
            self.next_rooms[room.name] = room

    def change_room(self, choice):

        if choice not in self.next_rooms.keys():
            print(f"{choice} it is not in the next room list")
            return self
        return self.next_rooms[choice]

    def __str__(self):
        return self.name
