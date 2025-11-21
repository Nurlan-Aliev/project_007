from bag_func import open_bag, select_item
from mini_game import get_round_data
from utils import input_data, join
from classes.npc import NPC, SnapeNPC
from classes.room import Room
from classes.hero import Hero
from item_list import *


def show_room_options(room: Room) -> str:
    print(room.next_rooms.keys())
    choices = ["bag", "look around", *room.next_rooms.keys()]
    if room.creature:
        choices.insert(1, f"talk with {room.creature}")
    if room.name == "Dungeon":
        choices.append("combine all items")
        choices.append("millstones")
    return input_data(f"What do you want?\n{join(choices)}")


def combine_items(hero):
    if hero.bag.is_in_bag(asphodel_leaves, pearl_dust, tears, moon_dust):
        print("Ураа получилось!")
    else:
        print("При смешивании ингрединетов все забурлило покраснело и взарвалось")
    quit()


def millstones(hero):
    print("Жернова заблокированы чтобы разблокировать нужно сыграть 3 игры")
    str_of_num, correct_answer = get_round_data()
    answer = input_data(
        join(("Нужно найти не достающее число", str_of_num), sep="")
    ).strip()
    if int(answer) != int(correct_answer):
        print("Не удалось разблокировать")
        return

    print("У тебя получилось")

    item = input_data(join(hero.bag)).lower()

    if item == moonstone.name.lower():
        hero.bag.remove(moonstone)
        hero.bag.add(moon_dust)
    else:
        print("Это нельзя размолоть")


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
    if choice == "combine all items":
        combine_items(hero)
        return room

    if choice == "millstones":
        if hero.bag.is_in_bag(moonstone):
            millstones(hero)
        return room

    if choice == "Professor Snake's office":
        next_room = room.change_room(choice)
        if tears in hero.bag:
            next_room.creature = None
        if isinstance(next_room.creature, SnapeNPC):
            next_room.creature.talk(hero)
            return room
        return next_room

    elif choice == "look around":
        look_around(room, hero)
        return room

    elif choice == "bag":
        open_bag(hero)
        return room

    elif "talk" in choice and isinstance(room.creature, NPC):
        room.creature.talk(hero)
        return room

    return room.change_room(choice)


def navigate_rooms(hero: Hero, rooms: Room):
    while True:
        print(rooms.clue)
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)
