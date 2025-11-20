from classes.hero import Gryffindor, Slytherin, Ravenclaw, Hufflepuff
from config import config
from launcher import navigate_rooms
from map import corridor
from utils import input_data, join


def beginning(name):
    hero_list = {
        "Slytherin": Slytherin,
        "Ravenclaw": Ravenclaw,
        "Hufflepuff": Hufflepuff,
        "Gryffindor": Gryffindor,
    }

    houses_text = join(hero_list)

    while True:
        hero = input_data(f"Choose a house\n{houses_text}")
        if hero in hero_list:
            return hero_list[hero](name)
        print("Invalid choice. Try again.")


def play_game():
    print(config.scenario.start)
    name = input_data("By the way what is your name my friend?")
    hero = beginning(name)
    navigate_rooms(hero, corridor)


if __name__ == "__main__":
    play_game()
