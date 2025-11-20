from item_list import tears, moon_light, asphodel_leaves, moonstone
from utils import input_data, join
import random
from config import config


class NPC:
    def __init__(self, name):
        self.name = name

    def talk(self, hero):
        pass

    def quest(self):
        pass

    def __str__(self):
        return self.name


class SnapeNPC(NPC):
    def __init__(self):
        super().__init__("Professor Snake")
        self.status = False

    def talk(self, hero):
        if self.status:
            print("Ты уже получил все что хотел. Иди отсюда!!")
            return
        if hero.house == "Slytherin":
            print(f"{self.name}: And what is it that you require, exactly?")
            answer = input_data(
                "Professor, can you give me recipe for the Moonlight Elixir?"
            ).lower()

            if "recipe" in answer:
                print(f"{self.name}: Here. Do try not to ruin it.\n")
                hero.bag.add(moon_light, asphodel_leaves, moonstone)
                self.status = True

            else:
                print(f"{self.name}: Begone.\n")

            return

        print(f"{self.name}: Why are you here? Get out!\n")


class PaintingNPC(NPC):
    def __init__(self):
        super().__init__("Living picture")
        self.status = False

    def talk(self, hero):
        if self.status:
            if tears in hero.bag:
                print(
                    f"{self.name}: Snape is in his office now. I don't recommend going in."
                )
            else:
                print(f"{self.name}: Snape's not here right now. You can go.")

        elif hero.house == "Hufflepuff":
            print(
                f"{self.name}: Hufflepuff, what did you want, my boy?\n"
                f"{hero.name}: Could you tell me when Professor Snape will not be in his office?\n"
                f"{self.name}: I'm bored with the picture here, guess the riddle and I'll help.\n"
            )
            self.quest()
        else:
            print(f"I don't intend to talk to anyone from the faculty {hero.house}")

    def quest(self):
        print("Зимой и летом одним цветом")

        answer = input_data().lower()

        if answer == "ёлка":
            print("I'll tell you when he's not there.")
            self.status = True
        else:
            print("Nooo, go think.")


class MirtleNPC(NPC):
    def __init__(self):
        super().__init__("Плакса Миртл")
        self.status = False

    def talk(self, hero):
        print(f"{self.name}: привет, {hero.name}, ты хочешь со мной поиграть?")
        answer = input_data()
        if "слез" in answer:
            print(f"{self.name} Я бы могла для тебя заплакать ты со мной сыграешь")
            self.status = self.quest()
            if self.status:
                print(
                    f"{self.name}:",
                    join(
                        (
                            f"Ой мне совсем не хочется плакать, но ты выиграл та что я помогу ты наверняка занешь мадам Лилейн",
                            "\t\t\tона сейчас скорее всего сидит в библиотеке попроси ее рассказать о ее муже и слезы точно будут",
                        ),
                        sep="",
                    ),
                )
        elif "да" in answer:
            self.quest()
        else:
            print(f"{self.name}: Не хочу ничего слышать если ты не хочешь играть")

    def quest(self):
        too_high_responses = [
            "Слишком много!",
            "Попробуй число поменьше.",
            "Нет, это выше загаданного.",
            "Перебор, уменьшай!",
            "Число меньше этого.",
        ]

        too_low_responses = [
            "Слишком мало!",
            "Попробуй число побольше.",
            "Нет, это ниже загаданного.",
            "Маловато будет, увеличь.",
            "Число больше этого.",
        ]
        guess_num = random.randint(1, 100)
        print(
            f"{self.name}: Правила очень просты я загадала число от 1 до 100 тебе нужно угадать я дам тебе 9 попыток это вполне реально"
        )
        for _ in range(8):
            number = int(input_data())
            if number > guess_num:
                print(random.choice(too_high_responses))
            elif number < guess_num:
                print(random.choice(too_low_responses))
            else:
                print(f"{self.name}: Ты победииил")
                return True
        else:
            print(f"{self.name}: Нееет, я загадывала {guess_num}")
            return False


class MadamLileynNPC(NPC):
    def __init__(self):
        super().__init__("Мадам Лилейн")
        self.status = False

    def talk(self, hero):
        if self.status:
            print("Спасибо что поговрил со мной")
            return

        print(f"привет, что ты хотел?")
        answer = input_data()
        if "муж" in answer and not self.status:
            print(self.name, config.npc.husband_story_madam_lileyn)
            print(f"{hero.name}: Я бы хотел собрать ваши слезы если вы не возражаете")
            self.status = True
            hero.bag.add(tears)
        else:
            print(
                f"{self.name}: не знаю о чем ты но расскажу тебе историю\n{random.choice(config.npc.stories_madam_lileyn)}"
            )
