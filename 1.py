# import math
# first_class = int(input('Введите кол-во учеников в первом классе: '))
# second_class = int(input('Введите кол-во учеников во втором классе: '))
# third_class = int(input('Введите кол-во учеников в третьем классе: '))
#
# print(f'1) {first_class} учеников \n'
#       f'2) {second_class} учеников \n'
#       f'3) {third_class} учеников \n'
#       f'Общее число: {first_class + second_class + third_class}')
#
# tables = (first_class + second_class + third_class) / 2
# print(math.ceil(tables))

numbers = [1, 2, 3, 4, 5, 6, 7]
way = input('В какую сторону едет поезд(вперёд/назад): ')
user_number = int(input('В какой вагон сел по ходу движения: '))

if way.lower() == 'вперёд':
      print(f'Номер вагона: {numbers[user_number - 1]}')


if way.lower() == 'назад':
      print(f'Номер вагона: {numbers[-user_number]}')

