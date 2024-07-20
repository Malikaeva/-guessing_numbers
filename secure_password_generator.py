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
            return True
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


count_password = int(is_valid(input('Укажите количество паролей для генерации: ')))
len_password = int(is_valid(input('Укажите длину пароля: ')))
digits_password = is_valid_yes_no(input(f'Включать ли цифры {digits}? '))
upper_password = is_valid_yes_no(input(f'Включать ли прописные буквы {uppercase_letters}? '))
lower_password = is_valid_yes_no(input(f'Включать ли строчные буквы {lowercase_letters}? '))
punctuation_pass = is_valid_yes_no(input(f'Включать ли символы {punctuation}? '))
ambiguous_characters_pass = is_valid_yes_no(input(f'Исключить неоднозначные символы {ambiguous_characters}? '))

list_1 = [digits, uppercase_letters, lowercase_letters, punctuation, ambiguous_characters]
list_2 = [digits_password, upper_password, lower_password, punctuation_pass, ambiguous_characters_pass]

for i in range(len(list_2)):
    if list_2[i]:
        char += list_1[i]

# if digits_password:
#     char += digits
# if upper_password:
#     char += uppercase_letters
# if lower_password:
#     char += lowercase_letters
# if punctuation_pass:
#     char += punctuation


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password


print(generate_password(len_password, char))

# for _ in range(count_password):
#     print(generate_password(len_password, char))