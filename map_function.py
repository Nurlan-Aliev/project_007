import item_list
import map
from mini_game import get_round_data
from utils import input_data, join


def office_func(hero):
    if item_list.tears in hero.bag:
        map.office.creature = None
        return map.office

    if map.office.creature:
        map.office.creature.talk(hero)
        return map.library


def dungeon_func(hero, choice):

    if choice == "combine all items":
        if not hero.bag:
            print("сумка пуста")
        else:
            combine_items(hero)

    if choice == "millstones":
        if hero.bag.is_in_bag(item_list.moonstone):
            millstones(hero)

    return choice


def combine_items(hero):
    if hero.bag.is_in_bag(
        item_list.asphodel_leaves,
        item_list.pearl_dust,
        item_list.tears,
        item_list.moon_dust,
    ):
        print(
            join(
                (
                    "Картины ликуют, как будто Гриффиндор взял Кубок Хогвартса",
                    "Едва ты заканчиваешь смешивать ингредиенты, котёл вспыхивает мягким серебристым светом — зелье готово.",
                    "И в тот же миг весь коридор буквально оживает: рамы дрожат, портреты высовываются вперёд, перекрикивая друг друга.",
                    "— «О-го-го! Он сделал это! Он действительно сделал это!",
                    "— «Это точно не Пуффендуй?!»",
                    "— «Оставь в покое Пуффендуй, просто у ребёнка талант!»",
                    "— «Пять баллов его факультету! Или десять! Ах, щедрость — моё второе имя!»",
                    "— «Если бы у меня были руки — я бы захлопал!»",
                    "— «Какой блеск… ах, сияние готового зелья… я такого не видел со времён молодого Дамблдора!",
                ),
                sep="",
            )
        )
    else:
        print("При смешивании ингрединетов все забурлило покраснело и взарвалось")
    quit()


def millstones(hero):
    print("Жернова заблокированы чтобы разблокировать нужно сыграть в игру")
    str_of_num, correct_answer = get_round_data()
    answer = input_data(
        join(("Нужно найти не достающее число", str_of_num), sep="")
    ).strip()
    if int(answer) != int(correct_answer):
        print("Не удалось разблокировать")
        return

    print("У тебя получилось")

    item = input_data(join(hero.bag)).lower()

    if item == item_list.moonstone.name.lower():
        hero.bag.remove(item_list.moonstone)
        hero.bag.add(item_list.moon_dust)
    else:
        print("Это нельзя размолоть")
