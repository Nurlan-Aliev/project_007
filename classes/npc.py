from utils import input_data, join
import random


class NPC:
    def __init__(self, name):
        self.name = name

    def talk(self, hero):
        pass

    def quest(self, hero):
        pass

    def __str__(self):
        return self.name


class SnapeNPC(NPC):
    def __init__(self):
        super().__init__("Professor Snake")

    def talk(self, hero):
        if hero.house == "Slytherin":
            print(f"{self.name}: And what is it that you require, exactly?")
            answer = input_data(
                join(
                    [
                        "Professor, would you be so kind as to share the recipe for the Moonlight Elixir?"
                    ]
                )
            ).lower()

            if "recipe" in answer:
                print(f"{self.name}: Here. Do try not to ruin it.\n")
            else:
                print(f"{self.name}: Begone.\n")
            return

        print(f"{self.name}: Why are you here? Get out!\n")


class PaintingNPC(NPC):
    def __init__(self):
        super().__init__("Living picture")
        self.status = False
        self.snape_in_room = True

    def talk(self, hero):
        if self.status:
            if self.snape_in_room:
                print(
                    f"{self.name}: Snape is in his office now. I don't recommend going in."
                )
            else:
                print(f"{self.name}: Snape's not here right now. You can go.")

    def quest(self, hero):
        if hero.house == "Hufflepuff":

            print(
                f"{self.name}: Hufflepuff, what did you want, my boy?\n"
                f"{hero.name}: Could you tell me when Professor Snape will not be in his office?\n"
                f"{self.name}: I'm bored with the picture here, guess the riddle and I'll help.\n"
                "Зимой и летом одним цветом"
            )

            answer = input_data().lower()

            if answer == "ёлка":
                print("I'll tell you when he's not there.")
                self.status = True
            else:
                print("Nooo, go think.")

        else:
            print(f"I don't intend to talk to anyone from the faculty {hero.house}")


class GhostNPC(NPC):
    def __init__(self):
        super().__init__("Living picture")
        self.status = False

    def talk(self, hero):
        guess_num = random.randint(1, 100)
        print("правила")
        for _ in range(8):
            number = int(input_data("твой вариант"))
            if number > guess_num:
                print("нет, это много")
            elif number < guess_num:
                print("нет, это мало")
            else:
                print("u win")
                break
        else:
            print("u lose")

    def quest(self, hero):
        if self.status:
            print("картины в коридоре прячут ключ. присмотрись")
        else:
            pass
