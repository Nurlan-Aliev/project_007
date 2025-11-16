from utils import input_data, join
from classes.npc import NPC, SnapeNPC
from classes.room import Room
from classes.hero import Hero


def show_room_options(room: Room) -> str:

    if room.creature:
        choices = join(["bag", f'talk with {room.creature}', *room.next_rooms.keys()])
    else:
        choices = join(["bag", *room.next_rooms.keys()])
    return input_data(f'What do you want?\n{choices}')


# def talk_to_npc(npc):
#     print(f"{npc.name}: {npc.next_phrase()}")
#     while not npc.is_finished():
#         answers = npc.await_answers()
#         hero_answer = input_data(answers).lower()
#
#         if not npc.react(hero_answer):
#             print(f"{npc.name}: {npc.do_not_understand()}")
#         else:
#             print(f"{npc.name}: {npc.next_phrase()}")

def look_around(room, hero):
    print()


def open_bag(hero):
    while True:

        options = join(["back", *hero.bag])
        choice = input_data(f'which item you want?\n{options}')
        if choice == "back":
            return

        for item in hero.bag:
            if item.name == choice:
                select_item(item, hero)
                break


def select_item(item, hero):
    while True:
        action = input_data(
            f"You chose {item.name}. What do you want?\n{join(['back','look','use','remove',])}"
        )
        if action == 'back':
            return

        elif action == 'look':
            item.look()

        elif action == 'use':
            pass

        elif action == 'remove':
            hero.bag.remove(item)
            return
        else:
            print('Pleas select from the list')


def handle_choice(hero, rooms, choice) -> Room:
    if choice == "Professor Snake's office":
        room = rooms.change_room(choice)
        if isinstance(room.creature, SnapeNPC) and hero.visible:
            room.creature.quest(hero)
            return rooms
        else:
            return room

    elif choice == "bag":
        open_bag(hero)
        return rooms

    elif 'talk' in choice and isinstance(rooms.creature, NPC):
        rooms.creature.quest(hero)
        return rooms

    else:
        print("The rooms is empty.")

    room = rooms.change_room(choice)
    return room


def navigate_rooms(hero: Hero, rooms: Room):
    while True:
        choice = show_room_options(rooms)
        rooms = handle_choice(hero, rooms, choice)
