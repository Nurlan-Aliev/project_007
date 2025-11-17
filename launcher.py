from bag_func import open_bag, select_item
from utils import input_data, join
from classes.npc import NPC, SnapeNPC
from classes.room import Room
from classes.hero import Hero


def show_room_options(room: Room) -> str:
    choices = ["bag", "look around", *room.next_rooms.keys()]
    if room.creature:
        choices.insert(1, f"talk with {room.creature}")

    return input_data(f"What do you want?\n{join(choices)}")


def look_around(room, hero):
    print(room.description)
    while True:
        options = join(["back", *room.items])
        choice = input_data(f"what do you want to take off?\n{options}")
        if choice == "back":
            return
        for item in room.items:
            if item.name == choice:
                select_item(item, hero, room)
                break


def handle_choice(hero, room, choice) -> Room:
    if choice == "Professor Snake's office":
        next_room = room.change_room(choice)
        if isinstance(next_room.creature, SnapeNPC) and hero.visible:
            next_room.creature.quest(hero)
            return room
        return next_room

    elif choice == "look around":
        look_around(room, hero)
        return room

    elif choice == "bag":
        open_bag(hero)
        return room

    elif "talk" in choice and isinstance(room.creature, NPC):
        room.creature.quest(hero)
        return room

    else:
        print("The rooms is empty.")

    return room.change_room(choice)


def navigate_rooms(hero: Hero, rooms: Room):
    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)
