from bag_func import open_bag, select_item
from map_function import office_func, dungeon_func
from mini_game import get_round_data
from utils import input_data, join
from classes.npc import NPC, SnapeNPC
from classes.room import Room
from classes.hero import Hero
from item_list import *


def show_room_options(room: Room):
    choices = ["bag", "look around", *room.next_rooms.keys()]
    if room.creature:
        choices.insert(1, f"talk with {room.creature}")
    if room.name == "Dungeon":
        choices.append("combine all items")
        choices.append("millstones")
    return input_data(f"What do you want? Choose from the list\n{join(choices)}")


def look_around(room, hero):
    print(room.description + "\n")
    while True:
        options = ["back", *room.items]
        if len(options) == 1:
            return
        choice = input_data(f"what do you want to take off?\n{join(options)}")
        if choice == "back":
            return
        for item in room.items:
            if item.name == choice:
                select_item(item, hero, room)
                break


def handle_choice(hero, room, choice):
    next_room = room.change_room(choice)

    if next_room.name == "Professor Snake's office":
        return office_func(hero)

    if next_room.name == "Dungeon":
        choice = dungeon_func(hero, choice)

    if choice == "look around":
        look_around(room, hero)

    if choice == "bag":
        open_bag(hero)

    if "talk" in choice and isinstance(room.creature, NPC):
        room.creature.talk(hero)

    return next_room


def navigate_rooms(hero: Hero, rooms: Room):
    while True:
        print(rooms.clue)
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)
