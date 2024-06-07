from random import randint


def guessing_game():
    hid_number = randint(1, 100)
    print('Введи число от 1 до 100.')
    cnt = 0  # кол-во попыток

    while True:
        num = input()

        # проверка числа
        while is_valid(num) == False:
            print('А может быть все-таки введем целое число от 1 до 100? (T-T)')
            num = input()
            cnt += 1

        if hid_number > int(num):
            print('Слишком мало, попробуйте еще раз')
            cnt += 1
        elif hid_number < int(num):
            print('Слишком много, попробуйте еще раз')
            cnt += 1
        else:
            print(f'''Вы угадали, поздравляем! ♡＼(￣▽￣)／♡
Количество догадок {cnt}''')
            break


# проверка на дурака
def is_valid(baka):
    abc = "abcdefghijklmnopqrstuvwxyz йцукенгшщзхфывапролджэячсмитьбю"

    flag = True

    for i in range(len(abc)):
        if abc[i] in baka:
            flag = False
            return flag

    if int(baka) < 1 or int(baka) > 100:
        flag = False

    return flag

    # if int(num) > 100 or int(num) < 1: может сделать отдельной функцией
    # реализовать проверку на дурака is_valid()


# повтор игры
def restart():
    print('Хочешь сыграть еще раз?')
    n = input().lower()
    while True:
        if n == 'да':
            guessing_game()
            print('Хочешь сыграть еще раз?')
            n = input().lower()
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся... ♡＾▽＾♡')
            break


# приветствие
print("""Добро пожаловать в 'Угадайку чисел'! ❤️❤️❤️
Вам нужно угадать загаданное число. (ㅇㅅㅇ❀)
Начинаем? 👍 (Напиши да)""")

hello = input().lower()

# запуск игры
while hello != "да":
    print("ХА-ХА-ХА, мы все равно начнем когда-нибудь 😂😂😂 ")
    hello = input().lower()
else:
    print("Поехали! 🚀 ")

guessing_game()
restart()
