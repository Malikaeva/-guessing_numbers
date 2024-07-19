import random

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase_letters = []
uppercase_letters = []
punctuation = []
char = ''


# реализовать проверку на дурака is_valid()
def is_valid(baka):
    if baka.isdigit():
        baka = int(baka)
        if 1 <= baka <= 100:
            return True
        else:
            return False
    else:
        return False