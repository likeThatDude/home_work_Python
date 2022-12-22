import random
# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2

def coins (n):
    coins_side = []
    for i in range(n):
        random_side = random.randint(0, 1)
        coins_side.append(random_side)

    eage_side = 0
    tails_side = 0
    for side in coins_side:
        if side == 0:
            eage_side += 1
        else:
            tails_side += 1

    min_side = 0
    if eage_side > tails_side:
        min_side = tails_side
    else:
        min_side = eage_side
    return f'Кол-во монеток лежащих орлом кверху: {eage_side}\n' \
           f'Кол-во монеток лежащих режкой кверху: {tails_side} \n' \
           f'Нужно перевернуть {min_side} монеток.'

numbers = int(input('Введите кол-во монеток: '))
print(coins(numbers))
# #
# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

x = random.randint(0, 1000)
y = random.randint(0, 1000)
print(f'Первое число: {x}\nВторое число: {y}')
s = x+y
print(f'Сумма: {s}')
p = x*y
print(f'Произведение: {p}')
count = s
while True:
    for i in range(s):
        if i * count == p:
            print(f'Петя загадал числа {i} и {count}')
            break
        else:
            count -= 1

# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
user_max_number = int(input('Введите число до которого будет возводится число 2 в степень: '))
count_three = 1
degree = []
degree_digit = []
while 2 ** count_three <= user_max_number:
    degree.append(count_three)
    degree_digit.append(2 ** count_three)
    count_three += 1
print(f'Выводим все степени в которые мы возводили: {degree}')
print(f'Выводим все 2-ки в стеспени: {degree_digit}')