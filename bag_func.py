from utils import join, input_data


def open_bag(hero):
    while True:

        options = join(["back", *hero.bag])
        choice = input_data(f"which item you want?\n{options}")
        if choice == "back":
            return

        for item in hero.bag:
            if item.name == choice:
                select_item(item, hero)
                break


def select_item(item, hero, room=None):
    options = ['back', 'look']

    if room:
        options.append('take it')
    else:
        options.append('remove')

    while True:
        action = input_data(
            f"You chose {item.name}. What do you want?\n{join(options)}"
        )

        if action not in options:
            print("Pleas select from the list")

        elif action == "back":
            return

        elif action == 'take it':
            item_transfer(room,hero,item)
            return

        elif action == "look":
            item.look()

        elif action == "use":
            pass

        elif action == "remove":
            hero.bag.remove(item)
            return


def item_transfer(room, hero, item):
    if item in room.items:
        if hero.bag.add(item):
            room.items.remove(item)
    else:
        print("it's not an object")
