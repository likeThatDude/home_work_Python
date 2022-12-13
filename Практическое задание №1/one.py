# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
a = 123
one = str(a)
sum = 0
count = 3

while count > 0:
    sum = sum + (a % 10)
    a = a // 10
    count -= 1

print(f'Сумма цифр трёхзначного числа: {one} -> {one[0]} + {one[1]} + {one[2]}  = {sum}')

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

number_of_cranes = int(input('Сколько журавликов всего сделали дети: '))
two_guys = (number_of_cranes / 100) * 33.33
petya = two_guys / 2
serhey = two_guys / 2
kate = (number_of_cranes / 100) * 66.67
print(f'Всего ребята сделали -> {number_of_cranes} журавлика(ов), Катя сделала: {round(kate)} журавликов, Петя: {round(petya)}, а Сергей: {round(serhey)}')

# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket_number = input('Введите 6-ти значный номер билетика: ')

while len(ticket_number) != 6:
    if len(ticket_number) > 6:
        ticket_number = input('''Номер не может быть БОЛЬШЕ 6-ти цифр, введите заново: ''')
    elif len(ticket_number) < 6:
        ticket_number = input('''Номер не может быть МЕНЬШЕ 6-ти цифр, введите заново: ''')

first_part = ticket_number[:3]
second_part = ticket_number[3:]
sum_one = 0
sum_two = 0

for i in first_part:
    sum_one = sum_one + int(i)
for i in second_part:
    sum_two = sum_two + int(i)

if sum_one == sum_two:
    print('Поздравляем =) у вас счастливый билетик!')
else:
    print('Поздравляем =) у вас счастливый билетик!')

# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input('Введите кол-во долек в длину:'))
length_size = length
width = int(input('Введите кол-во долек в ширину:'))
width_size = width
segment = int(input('Сколько долек вы хотите отломить:'))
count = 1
width_plus = width
print(f'И так у вас получилась шоколадка размером: {length} на {width} долек '
      f'Сейчас попробуем отломить от её {segment} долек и посмотрим получится ли у нас.')
print('Минуточку, пробую отломить по длине.')

while length_size > 0 or width_size != segment:
    if width_size == segment:
        print(f'Отлично у нас получилось отломить {count} полоску(ки) сверху шоколадки,'
              f'там как раз было {segment} дольки(ек)')
        break
    else:
        length_size -= 1
        width_size = width_size + width
        count += 1
    if length_size == 1:
        print(f'И так, по длине у нас не получилось, будем пробовать по ширине')
        break

length_size = length
width_plus = width
count = 1

while width_size > 0 or length_size != segment:
    if length_size == segment:
        print(f'Отлично у нас получилось отломить {count} полоску(ки) сбоку шоколадки,'
              f'там как раз было {segment} дольки(ек)')
        break
    else:
        width_size -= 1
        length_size = length_size + length
        count += 1
    if width_size == 1:
        print(f'Увы но и по ширине у нас ничего не вышло.')
        break

