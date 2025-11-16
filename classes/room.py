class Room:
    def __init__(self, name, creature=None):
        self.name = name
        self.creature = creature
        self.next_rooms = {}

    def add_room(self, *args):
        for room in args:
            self.next_rooms[room.name] = room

    def change_room(self, choice):

        if choice not in self.next_rooms.keys():
            print(f"{choice} it is not a room")
            return self
        return self.next_rooms[choice]

    def __str__(self):
        return self.name
