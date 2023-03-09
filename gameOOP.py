"""
This module represent game in OOP paradigm.
"""
import json
import requests


REGIM = ''

class Game:
    """
    This class represent a game as an instance.
    """
    def __init__(self) -> None:
        self.number_of_tries = None
        self.user_name = None

    def main(self) -> None:
        """ 

        Function, that started the game and asks user's name and difficulty. 
        Then functiuon redirects user to first_task() function

        :param: None
        :return: None
        """

        print('Привіт! На вулиці 2356 рік і світ стоїть на межі'
            ' глобальної каqтастрофи ядерного удару. Але саме ти можеш його врятувати.' 
            " У тебе мало часу і майже немає права на помилку."
            " Для початку скажи, як ти хочеш, щоб тебе називали,"
            " ми ж маємо знати рятівника світу в лице)")
        users_name = input('>>> ')
        self.user_name = users_name
        print(f"{users_name.capitalize()}, звучить по-геройськи!"
            " Тепер вибери режим складності (1 - hard, 2 - medium, 3 - easy)")
        difficulty = int(input(">>> "))
        if difficulty == 1:
            self.number_of_tries = 1
        elif difficulty == 2:
            self.number_of_tries = 2
        elif difficulty == 3:
            self.number_of_tries = 3
        else:
            print('Такого режиму складності немає! Спробуй ще раз!')

    def time_remaining(self) -> None:
        """

        Function, that makes countdown to the bomb explosion.
        Countdown starts from 5 sec.

        :param: None
        :return: None
        """

        for i in range(5):
            if 5 - i == 5:
                print(str(5 - i) + ' секунд лишилось')
            elif 5 - i == 1:
                print(str(5 - i) + " секунда лишилась")
            else:
                print(str(5 - i) + " секунди лишилось")
        print(" ____   ____   ____  __  __ ")
        print("|  _ \ / __ \ / __ \|  \/  | ")
        print("| |_) | |  | | |  | | \  / |")
        print('|  _ <| |  | | |  | | |\/| |')
        print('| |_) | |__| | |__| | |  | |')
        print('|____/ \____/ \____/|_|  |_|\n')
        return


class FirstTask:
    """
    This class represent first task.
    """
    def first_task(self, other) -> None:
        """
        
        Function, that gives user the first task.
        User has different amount of tries depending on level, that he chose in the function main()
        Function can redirect user to time_remaining or to second_task function.
        
        :param name:
        :param number_of_tries:
        :return None:
        """

        if other.number_of_tries == 1:
            global REGIM
            REGIM = 'hard'
        elif other.number_of_tries == 2:
            REGIM = 'medium'
        else:
            REGIM = 'easy'
        print("Отже, {name}, ти вибрав {regim} режим, в тебе є {tries} спроби(-а)."
            " Отож, вперед рятувати світ!\n\n"
            "*************************************\n\n"
            "Перш за все тобі треба перестрахуватись і дізнатись скільки у тебе є часу."
            " Атомні бомби виготовляють з ізотопу Урану-235, період піврозпаду якого становить 26 хв."
            " Скажи, за скільки хвилин розпадеться три"
            " четвертих ядер Урану-235?".format(name=other.user_name.capitalize(), regim=REGIM, tries=other.number_of_tries))
        while other.number_of_tries > 0:
            answer = float(input(">>> "))
            if answer != 52:
                other.number_of_tries -= 1
                if number_of_tries == 0:
                    print("На жаль, відповідь не вірна. Тобі не вдалося врятувати світ.\n")
                    self.time_remaining()
                    break
                else:
                    print('Подумай ще. В тебе лишилась(-ись) {tries} спроба(-и)'\
                          .format(tries=other.number_of_tries))
            else:
                print('Чудово! Рухаємося далі.\
 Ми вже за декілька кроків до запобігання катастрофи!\n\n')
                break

    def time_remaining(self) -> None:
        """

        Function, that makes countdown to the bomb explosion.
        Countdown starts from 5 sec.

        :param: None
        :return: None
        """

        for i in range(5):
            if 5 - i == 5:
                print(str(5 - i) + ' секунд лишилось')
            elif 5 - i == 1:
                print(str(5 - i) + " секунда лишилась")
            else:
                print(str(5 - i) + " секунди лишилось")   
        print(" ____   ____   ____  __  __ ")
        print("|  _ \ / __ \ / __ \|  \/  | ")
        print("| |_) | |  | | |  | | \  / |")
        print('|  _ <| |  | | |  | | |\/| |')
        print('| |_) | |__| | |__| | |  | |')
        print('|____/ \____/ \____/|_|  |_|\n')


class SecondTask:
    """
    This class represent second task.
    """
    def second_task(self, other) -> None:
        """

        Function, that gives user the second task.
        User has different amount of tries depending on level, that he chose in the function main()
        Function can redirect user to time_remaining or to final_task function.

        :param name:
        :param counter_of_choices:
        :return None:
        """

        print(f"Отже, {other.user_name.capitalize()}, ти вже знаєш скільки у "
            f"тебе є часу. Тепер потрібно добратись до місця запуску ракети, щоб детонувати її.\n")
        print("*************************************\n")
        print("Ти прибув за адресою в лабораторію і "
            "збираєшся зайти в ліфт. Відомо,\
 що номер поверху, на якому знаходиться апарат для запуску ракети"
            "дорівнює числу '3' в двіковій системі числення.\
 То яку кнопку тобі потрібно натиснути?")

        while other.number_of_tries != 0:
            answer = int(input(">>> "))
            if answer != 11:
                other.number_of_tries -= 1
                if other.number_of_tries == 0:
                    print('\nТи був близький, але тобі не вдалося піднятися на потрібний поверх\n')
                    self.time_remaining()
                    break
                else:
                    print('\nНевірно. В тебе лишилась {tries} спроба(-и).\
 Подумай ще, час іде'.format(tries=other.number_of_tries))
            else:
                print('\nEasy peasy lemon squeezy! Рухаємось далі, залишилось зовсім трошки!')
                break

    def time_remaining(self) -> None:
        """

        Function, that makes countdown to the bomb explosion.
        Countdown starts from 5 sec.

        :param: None
        :return: None
        """

        for i in range(5):
            if 5 - i == 5:
                print(str(5 - i) + ' секунд лишилось')
            elif 5 - i == 1:
                print(str(5 - i) + " секунда лишилась")
            else:
                print(str(5 - i) + " секунди лишилось")   
        print(" ____   ____   ____  __  __ ")
        print("|  _ \ / __ \ / __ \|  \/  | ")
        print("| |_) | |  | | |  | | \  / |")
        print('|  _ <| |  | | |  | | |\/| |')
        print('| |_) | |__| | |__| | |  | |')
        print('|____/ \____/ \____/|_|  |_|\n')


class FinalTask:
    """
    This class represent final task.
    """
    def final_task(self, other) -> None:
        """

        Function, that gives user the final task.
        User has only one try, all previous tries reset to zero.
        Function can redirect user to time_remaining function or ask user does he want to celebrate.
        
        :param name:
        :return None:
        """
        if other.number_of_tries == 0:
            return
        print("*************************************\n\n") 

        print(f"{other.name.capitalize()}, ти піднявся на потрібний поверх\
 і бачиш перед собою величезний комп'ютер,"
            " на головному екрані якого зображена форма для введення пін-коду."
            " У тебе є лиш одна спроба ввести правильний пін."
            " Поки що ти його не знаєш, однак на\
 столі лежать 3 конверти, в одному з яких правильний пін-код."
            "Але є одна проблема: в одному із конвертів написана лиш правда,"
            " в іншому лише брехня, а в третьому одне твердження - брехня, інше - правда" 
            "На першому конверті написано:\n")
        print("1. Не відкривай цей конверт\n2. Обов'язково відкрий другий конверт\n\n")
        print("На другому конверті написано:\n")
        print("1. Не треба відкривати перший конверт\n2. Відкривай третій конверт\n\n")
        print('На третьому конверті написано:\n')
        print("1. Не відкривай цей конверт\n2. Відкривай перший конверт\n\n")
        print('Після того як ти опрацював ці твердження і зрозумів, '
            'що не дарма ходив на практику з дискретної\
 математики до пані Юлії ти вибираєш конверт №:')
        answer = int(input(">>> "))
        if answer == 1 or answer == 2:
            print("Відкривши конверт, ти бачиш число 2508.\
 Тож вперед рятувати світ! Введи пін код швидше, час іде!\n")
            pin = input('>>> ')
            print('На жаль, пін-код невірний, адже ти вибрав неправильний конверт.')
            self.time_remaining()
        if answer == 3:
            print("Відкривши конверт, ти бачиш число 0310.\
 Тож вперед рятувати світ! Введи пін код швидше, час іде!")
            pin = input(">>> ")
            if pin != '0310':
                print('Ти був так близько, але ти ввів неправильний пін-код')
                self.time_remaining()
            else:
                print('\n\n███    ███ ██ ███████ ███████ ██  ██████  ███    ██      ██████  ██████  ███    ███ ██████  ██      ███████ ████████ ███████ ██████ ')
                print('████  ████ ██ ██      ██      ██ ██    ██ ████   ██     ██      ██    ██ ████  ████ ██   ██ ██      ██         ██    ██      ██   ██ ')
                print('██ ████ ██ ██ ███████ ███████ ██ ██    ██ ██ ██  ██     ██      ██    ██ ██ ████ ██ ██████  ██      █████      ██    █████   ██   ██ ')
                print('██  ██  ██ ██      ██      ██ ██ ██    ██ ██  ██ ██     ██      ██    ██ ██  ██  ██ ██      ██      ██         ██    ██      ██   ██ ')
                print('██      ██ ██ ███████ ███████ ██  ██████  ██   ████      ██████  ██████  ██      ██ ██      ███████ ███████    ██    ███████ ██████  \n')
                print("Браво! Щойно ти потрапив в історію, як людина яка врятувала світ! "
                    " Тепер можна це відсвяткувати і випити святковий коктейль!)\n\n")
                print("(1) - Що? Навіщо це мені?\
 Я хочу якнайшвидше бути вільним. Порятунок світу - виснажлива справа.")
                print("(2) - Звучить цікаво, давай!\n")
                choice = int(input(">>> "))
                while choice != 1 or choice != 2:
                    if choice == 1:
                        self.end_game(name)
                        break
                    elif choice == 2:
                        self.coctail(name)
                        break
                    else:
                        print('Спробуй ще раз! Ти помилився з вибором)')
                        choice = int(input(">>> "))

    def end_game(self, name: str) -> None:
        """
        Function, that ends the game
        :param: name
        :return: None
        """
        print(f"Отже, {name.capitalize()}, весь наш штаб виносить"
        " тобі подяку та повагу за порятунок світу. На тебе можна покластись. Щасти тобі!")

    def coctail(self, name: str) -> None:
        """
        Function, that parse information from open API
        (source=https://www.thecocktaildb.com/api.php)
        and shows is's name
        :param: name
        :return: None
        """
        print('******************\n')
        print(f"{name.capitalize()}, тільки тобі і\
 тільки сьогодні паб дарує свій фірмовий коктейль!\n")
        link = r"https://www.thecocktaildb.com/api/json/v1/1/random.php"
        data = requests.get(link)
        coctail_info = json.loads(data.text)
        drink = coctail_info.get('drinks')
        print('Твій коктейль:\n')
        print(drink[0].get('strDrink').upper())

    def time_remaining(self) -> None:
        """

        Function, that makes countdown to the bomb explosion.
        Countdown starts from 5 sec.

        :param: None
        :return: None
        """

        for i in range(5):
            if 5 - i == 5:
                print(str(5 - i) + ' секунд лишилось')
            elif 5 - i == 1:
                print(str(5 - i) + " секунда лишилась")
            else:
                print(str(5 - i) + " секунди лишилось")
        print(" ____   ____   ____  __  __ ")
        print("|  _ \ / __ \ / __ \|  \/  | ")
        print("| |_) | |  | | |  | | \  / |")
        print('|  _ <| |  | | |  | | |\/| |')
        print('| |_) | |__| | |__| | |  | |')
        print('|____/ \____/ \____/|_|  |_|\n')
        return


if __name__ == '__main__':
    main_game = Game()
    main_game.main()
    number_of_tries = main_game.number_of_tries
    name = main_game.user_name
    first_task = FirstTask()
    first_task.first_task(main_game)
    secondtask = SecondTask()
    secondtask.second_task(main_game)
    finaltask = FinalTask()
    finaltask.final_task(main_game)
