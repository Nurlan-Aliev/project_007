from item_list import tears, moonlight_recept, asphodel_leaves, moonstone
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
                hero.bag.add(asphodel_leaves, moonstone)
                self.status = True

            else:
                print(f"{self.name}: Begone.\n")

            return

        print(
            f"{self.name}: Какая удача встретить вас здесь мне как раз нужна была ваша помошь тем чтобы перетаскать все эти книги\n"
        )
        print(
            "снейп заставил тебя с таскать кники весь день и ты не успел приготовить зелье"
        )
        quit()


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

        elif hero.house != "Slytherin":
            print(
                f"{self.name}: what did you want, my boy?\n"
                f"{hero.name}: Could you tell me when Professor Snape will not be in his office?\n"
                f"{self.name}: I'm bored with the picture here, guess the riddle and I'll help.\n"
            )
            self.quest()
        else:
            print(f"I don't intend to talk to anyone from the faculty Slytherin")

    def quest(self):
        print("Маленький, золотой, в воздухе свищу. Поймаешь меня — победу принесу.")

        answer = input_data().lower()

        if answer == "снитч":
            print("I'll tell you when he's not there.")
            self.status = True
        else:
            print("Nooo, go think.")


class MirtleNPC(NPC):
    def __init__(self):
        super().__init__("Плакса Миртл")
        self.tears_status = False
        self.snape_status = False

    def talk(self, hero):
        answers = []
        if not self.tears_status:
            answers.append("can you lend me your tears")

        print(f"{self.name}: hi, {hero.name}, ты хочешь со мной поиграть?")
        answer = input_data(join(answers)).lower()

        if "tear" in answer:
            if self.tears_status:
                print(
                    "я же сказала что слезу можно взять у Лилейн если спросить о ее муже"
                )
            print(f"{self.name} Я бы могла для тебя заплакать ты со мной сыграешь")
            self.tears_status = self.guest_number()
            if self.tears_status:
                print(
                    f"{self.name}:",
                    join(
                        (
                            f"Ой мне совсем не хочется плакать, но ты выиграл та что я помогу ты наверняка занешь мадам Лилейн",
                            "       она сейчас скорее всего сидит в библиотеке попроси ее рассказать о ее муже и слезы точно будут",
                        ),
                        sep="",
                    ),
                )

        elif "да" in answer:
            self.guest_number()
        else:
            print(f"{self.name}: Не хочу ничего слышать если ты не хочешь играть")

    def guest_number(self):
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
        for _ in range(9):
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
            print(
                f"{hero.name}: Мадам Лилейн, позволите мне собрать одну вашу слезу? В ней больше света, чем в половине заклинаний Хогвартса."
            )
            self.status = True
            hero.bag.add(tears)
        else:
            print(
                f"{self.name}: не знаю о чем ты но расскажу тебе историю\n{random.choice(config.npc.stories_madam_lileyn)}"
            )
