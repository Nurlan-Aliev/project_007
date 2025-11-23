from classes.bag import Bag
from utils import input_data


class Room:
    def __init__(self, name, description, clue="", creature=None, blocked=False):
        self.name = name
        self.description = description
        self.creature = creature
        self.next_rooms = {}
        self.items = Bag()
        self.blocked = blocked
        self.clue = clue

    def add_room(self, *args):
        for room in args:
            self.next_rooms.update(room)

    def change_room(self, choice):
        if choice not in self.next_rooms.keys():
            return self

        if self.next_rooms[choice].blocked:
            print("this room is blocked")
            answer = input_data("Maybe you know a spell to open the door?")
            if answer.lower() != "alohomora":
                return self
            self.blocked = False

        return self.next_rooms[choice]

    def __str__(self):
        return self.name
