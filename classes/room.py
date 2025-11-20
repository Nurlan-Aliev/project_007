from classes.bag import Bag
from utils import input_data


class Room:
    def __init__(self, name, description, creature=None, blocked=False):
        self.name = name
        self.description = description
        self.creature = creature
        self.next_rooms = {}
        self.items = Bag()
        self.blocked = blocked

    def add_room(self, *args):
        for room in args:
            self.next_rooms[room.name] = room

    def change_room(self, choice):
        if choice not in self.next_rooms.keys():
            print(f"{choice} it is not in the next room list")
            return self

        if self.next_rooms[choice].blocked:
            print("this room is blocked")
            answer = input_data("Do you have key?")
            if answer.lower() != "alohomora":
                return self
            self.blocked = False
            return self.next_rooms[choice]

        return self.next_rooms[choice]

    def __str__(self):
        return self.name
