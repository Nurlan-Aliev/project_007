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
    print(
        "Профессор Вуд дает задание приготовить зелье лунного света. Нам нужно подготовиться к следующему уроку, до которого",
        "осталось совсем немного времени. Правда, я полностью про это забыл, и теперь времени у меня почти не осталось.",
        "Ко всему прочему, профессор ничего не говорит о том, где искать ингредиенты, как готовить зелье и даже из чего оно состоит.",
        "Он предлагает нам самим найти рецепт и приготовить это зелье. Что ж, мне кажется, лучший способ начать — отправиться в библиотеку.",
        "Возможно, в книгах я найду какую-нибудь подсказку, которая поможет справиться с этим заданием.",
        "Главное — успеть собрать все ингредиенты и прийти в кабинет профессора Вуда.\n",
        sep="\n",
    )

    name = input_data("By the way what is your name my friend?")
    hero = beginning(name)
    navigate_rooms(hero, corridor)


if __name__ == "__main__":
    play_game()
