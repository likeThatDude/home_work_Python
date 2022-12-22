import random
import math
from langdetect import detect

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
#
# Ввод: 5
# Ввод: 1
#
# 1 2 1 2 2
# Вывод: 2

# user_input_number = int(input('Введите число для определения размера массива: '))
# check_digit = int(input('Введите число которое нужно проверить: '))
# print(
#     f'И так, размер будет равен вашему числу: {user_input_number} делённому на 2. (округление будет в большую сторону)')
#
# digit_for_list = math.ceil(user_input_number / 2)
# random_list = []
#
# while digit_for_list > 0:
#     random_list.append(random.randint(1, user_input_number))
#     digit_for_list -= 1
# print('Ваш массив состоит из данных чисел: ', end=' ')
# print(*random_list, sep=', ')
#
# count = 0
# for i in random_list:
#     print(type(i))
#     if i == check_digit:
#         count += 1
#     else:
#         continue
#
# print(f'Ваше число: {check_digit}, встречается в массиве: {count} раз.')

# Задача 18:
# # Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# # Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# # Заполните массив случайными натуральными числами от 1 до N.
# # Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# #
# # Ввод: 10
# # Ввод: 7
# # 1 2 1 8 9 6 5 4 3 4
# # Вывод: 6
#
#
# user_list_digit = int(input('Введите число для определения размера массива: '))
# check_list_digit = int(input('Введите число которое нужно проверить: '))
# user_list = []
# list_count = user_list_digit
#
# while list_count > 0:
#     user_list.append(random.randint(0, user_list_digit))
#     list_count -= 1
# print(user_list)
#
# if check_list_digit in user_list:
#     print(f'Число {check_list_digit} есть в списке. Но оно нам не подходит')
#
# digit_in_list_minus = check_list_digit - 1
# digit_in_list_plus = check_list_digit + 1
# while True:
#     if digit_in_list_minus in user_list:
#         break
#     else:
#         digit_in_list_minus -= 1
#
# while True:
#     if digit_in_list_plus in user_list:
#         break
#     else:
#         digit_in_list_plus += 1
#
# if check_list_digit - digit_in_list_minus == abs(check_list_digit - digit_in_list_plus):
#     print(f'В списке два числа одинаково близких к вашему: \n1) {digit_in_list_plus}\n2) {digit_in_list_minus}')
# elif check_list_digit - digit_in_list_minus < abs(check_list_digit - digit_in_list_plus):
#     print(f'Ближайшее число: {digit_in_list_minus}')
# elif check_list_digit - digit_in_list_minus > abs(check_list_digit - digit_in_list_plus):
#     print(f'ближайшее число: {digit_in_list_plus}')

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# Ввод: ноутбук
# Вывод: 12

letters = {
     "AEIOULNSTRАВЕИНОРСТ": 1,
     "DGДКЛМПУ": 2,
     "BCMPБГЁЬЯ": 3,
     "FHVWYЙЫ": 4,
     "KЖЗХЦЧ": 5,
     "JXШЭЮ": 8,
     "QZФЩЪ": 10
          }

user_word = input('Введите ваше слово: ')
eng_letter = []
rus_letter = []

while True:
    while len(user_word) == 0:
        user_word = input('Введите ваше слово (Поле не должно быт пустым): ')

    for i in user_word:
        if ord(i.upper()) in range(65, 91):
            eng_letter.append(ord(i.upper()))
        if ord(i.upper()) in range(1040, 1072):
            rus_letter.append(ord(i.upper()))
    if len(eng_letter) == len(user_word):
        print(f'Ваше слова на латинице, в нём {len(eng_letter)} букв(ы).')
        break
    elif len(rus_letter) == len(user_word):
        print(f'Ваше слова на кириллице, в нём {len(rus_letter)} букв(ы).')
        break
    else:
        user_word = input('Введите слово используя буквы одного из двух алфавитов (латиница, кириллица): ')

letters_sum = []

for i in user_word:
    for key in letters.keys():
         if i.upper() in key:
              letters_sum.append(letters[key])

print(f'Сумма букв вашего слова, согласно условию задачи: {sum(letters_sum)}')
