from classes.hero import Gryffindor,Slytherin,Ravenclaw,Hufflepuff
from launcher import navigate_rooms
from map import dungeon, corridor
from utils import input_data, join

from classes.items import Note

note = Note('potion recipe', "Take some onion, fry it over medium heat, and you'll have fried onions.")


def beginning(name):
    hero_list = {
        "Slytherin": Slytherin,
        "Ravenclaw": Ravenclaw,
        "Hufflepuff": Hufflepuff,
        'Gryffindor': Gryffindor
    }

    houses_text = join(hero_list)

    # while True:
    #     hero = input_data(f"Choose a house\n{houses_text}")
    #     if hero in hero_list:
    #         return hero_list[hero](name)
    #     print("Invalid choice. Try again.")
    return Hufflepuff(name)


def play_game():
    name = input_data('What is your name my friend?')
    hero = beginning(name)
    hero.bag.add(note)
    hero.bag.add(note)
    # navigate_rooms(hero, dungeon)
    navigate_rooms(hero, corridor)


if __name__ == "__main__":
    play_game()
