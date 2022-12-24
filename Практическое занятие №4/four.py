import random
import math

# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
#
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
#
# Output: 11 6
# 6 12
#
n = int(input('Количество цифр в первом списке: '))
m = int(input('Количество цифр во втором списке: '))

first_list = []
second_list = []
new_list = []

for i in range(n):
    first_list.append(random.randint(0, n))

for i in range(m):
    second_list.append(random.randint(0, m))

print(f'{first_list}\n{second_list}')


for i in first_list:
    if i in second_list:
        new_list.append(i)

new_list = set(new_list)
print('Отсортированный список из двух: ', end='')
print(*new_list,sep=', ')

# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#
# Input: 4
# (значения сгенерированы случайным образом)
# 4 2 3 1 )
#
# Output: 9

amt_bush = int(input('Введите кол-во кустов на грядке: '))
bush_dic = []

count = 1
for i in range(0, amt_bush):
    bush_dic.append(random.randint(0, 100))
    if bush_dic[count - 1] > 0:
        print(f'На кусте <{count}> выросло: {bush_dic[count - 1]} ягод')
    else:
        print(f'На кусте <{count}> выросло: {bush_dic[count - 1]} ягод. Фермер будет расстроен.')
    count += 1

amt_berrys = 0
bush_index = 0
index = 0

for i in bush_dic:
    if index == len(bush_dic) - 1:
        if bush_dic[index] + bush_dic[index - 1] + bush_dic[0] > amt_berrys:
            amt_berrys = bush_dic[index] + bush_dic[index - 1] + bush_dic[0]
            bush_index = index + 1
        else:
            amt_berrys = amt_berrys
        break
    if index <= len(bush_dic) - 2:
        if bush_dic[index] + bush_dic[index - 1] + bush_dic[index + 1] > amt_berrys:
            amt_berrys = bush_dic[index] + bush_dic[index - 1] + bush_dic[index + 1]
            bush_index = index + 1
    index += 1

print(f'Самое большое кол-во ягод будет собранно, если центральным кустом будет: {bush_index}. ')
print(f'Количество ягод в таком случае будет: {amt_berrys} штук')

# Задача 101
#Вычислить число π c заданной точностью d
# # Пример:
# # при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
#
pi = math.pi
user_digit = int(input(f'Здравствуйте, с какой точностью (кол-во знаков после запятой) вывести число π : '))
print(f'Ваш результат: {round(pi, user_digit)}')

# Задача 102
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
user_digit_n = int(input('Введите число которое нужно разложить на простые множители: '))

last_digit = user_digit_n
finish_digit = []

for i in range(2, user_digit_n):
    if last_digit / i == 1:
        finish_digit.append(i)
        break
    while True:
        if last_digit % i == 0:
            finish_digit.append(i)
            last_digit /= i
        else:
            break
print('вот полный список натуральных чисел вашего числа: ', end=(''))
print(*finish_digit, sep=' х ', end=' = ')
print(user_digit_n)

