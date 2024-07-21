import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_characters = 'il1Lo0O'
char = ''


# реализовать проверку на дурака is_valid()
# проверка на число
def is_valid(baka):
    while True:
        if baka.isdigit() and int(baka) > 0:
            return int(baka)
        else:
            baka = input('Повторите ввод числа: ')


# Проверка да или нет
def is_valid_yes_no(baka):
    while True or False:
        if baka.lower() == 'да':
            return True
        elif baka.lower() == 'нет':
            return False
        else:
            baka = input('Напишите да / нет: ')
        # Вариант через case
        # match baka.lower():
        #     case 'да':
        #         return True
        #     case 'нет':
        #         return False
        #     case _:
        #         baka = input('Напишите да / нет: ')


count_password = is_valid(input('Укажите количество паролей для генерации: '))
len_password = is_valid(input('Укажите длину пароля: '))
digits_password = is_valid_yes_no(input(f'Включать ли цифры {digits}? '))
upper_password = is_valid_yes_no(input(f'Включать ли прописные буквы {uppercase_letters}? '))
lower_password = is_valid_yes_no(input(f'Включать ли строчные буквы {lowercase_letters}? '))
punctuation_pass = is_valid_yes_no(input(f'Включать ли символы {punctuation}? '))
ambiguous_characters_pass = is_valid_yes_no(input(f'Исключить неоднозначные символы {ambiguous_characters}? '))

list_1 = [digits, uppercase_letters, lowercase_letters, punctuation, ambiguous_characters]
list_2 = [digits_password, upper_password, lower_password, punctuation_pass, ambiguous_characters_pass]

for i in range(len(list_2) - 1):
    if list_2[i]:
        char += list_1[i]


# if ambiguous_characters_pass:
#     for ambiguous_characters in char:
#
# print(char)


def generate_password(length, chars):
    password = ''
    while len(password) == length:
        password += random.choice(chars)
        if ambiguous_characters_pass:
            if password[-1] in ambiguous_characters:
                password = password[:-1]
    return password


print(generate_password(len_password, char))

# for _ in range(count_password):
#    print(generate_password(len_password, char))
