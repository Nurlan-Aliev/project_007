from utils import input_data, join


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

    def quest(self, hero):
        self.talk(hero)


class PaintingNPC(NPC):
    def __init__(self):
        super().__init__("Living picture")
        self.status = False
        self.snape_in_room = True

    def talk(self, hero):
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

    def quest(self, hero):
        if self.status:
            if self.snape_in_room:
                print(f"{self.name}: Снейп сейчас в кабинете. Не советую заходить.")
            else:
                print(f"{self.name}: Снейпа сейчас нет. Можешь идти.")
        else:
            self.talk(hero)
