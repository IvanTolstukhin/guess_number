# Правила игры:
# Компьютер случайным образом выбирает число в указанном диапазоне.
# Игрок вводит в терминале своё предположение относительно этого числа.
# Программа сравнивает выбор игрока с загаданным числом.
# В ответ выводится одно из трёх сообщений:
# «Ваше число меньше того, что загадано»;
# «Ваше число больше того, что загадано»;
# «Отличная интуиция! Вы угадали число :)».
# Если предположение оказалось неверным, программа предложит попробовать снова.
# Игра будет продолжаться, пока игрок не угадает загаданное число.

from random import randint


def create_number():
    number = randint(1, 100)
    get_user_number(number)


def get_user_number(number):
    user_num = int(input())
    check_number(user_num, number)


def check_number(user_num, number):
    if type(user_num) is not int or user_num < 0 or user_num > 100:
        print(f'{str(user_num)} - не подходит! Введите число от 1 до 100!')
        get_user_number(number)
    elif user_num == number:
        print('Отличная интуиция! Вы угадали число :)')
        create_number()
    elif user_num > number:
        print('Ваше число больше того, что загадано :(')
        get_user_number(number)
    elif user_num < number:
        print('Ваше число меньше того, что загадано :(')
        get_user_number(number)
    else:
        print('Что-то пошло не так')
        get_user_number(number)


create_number()
