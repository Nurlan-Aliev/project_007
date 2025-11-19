from classes.hero import Gryffindor, Slytherin, Ravenclaw, Hufflepuff
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
    print('Ты находишься в коридоре с живыми картинами Хогвартса. Сейчас идут уроки поэтому тут никого нет.\n'
          'Тебе нужно приготовить зелье НАЗВАНИЕ ЗЕЛЬЯ. это достаточно сложное зелье и не каждому волшебнику дано его приготовить.\n'
          'попробуй начать с библиотеки может там ты найдешь какие то подсказки\n'
          'И постарайся не попадаться на глаза преподователям\n')
    name = input_data("By the way what is your name my friend?")
    hero = beginning(name)
    navigate_rooms(hero, corridor)


if __name__ == "__main__":
    play_game()
