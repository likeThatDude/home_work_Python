import random
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

# n = int(input('Введите число: '))
#
# factorial = 1
#
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)
# 0 1 1 2 3 5 8 13 21
# def fibonache(user_number):
#     if user_number == 0:
#         return 'Номер вашего числа в последовательности 1'
#     if user_number == 1:
#         return 'Номер вашего числа в последовательности 2 и 3'
#
#     number_one = 0
#     number_two = 1
#     count = 2
#     sum = number_one + number_two
#
#     while user_number > number_two:
#         sum = number_one + number_two
#         number_one = number_two
#         number_two = sum
#         count += 1
#
#     if user_number == number_two:
#         return f'Номер вашего числа в последовательности {count}'
#     if user_number < number_two:
#         return f'Ваше число {user_number} не является числом фибоначи'
#
# user_number = int(input('Input digit: '))
# print(fibonache(user_number))

# days = int(input('Введите кол-во дней: '))
# all_temp =[]
#
# for i in range(days):
#     random_digit = random.randint(-50, 50)
#     all_temp.append(random_digit)
# print(all_temp)
#
# plus_temp = []
# count = 0
# max_days_one = 0
# max_days_two = 0
# while days > 0:
#     if all_temp[count] > 0:
#         plus_temp.append(all_temp[count])
#         max_days_one += 1
#     elif all_temp[count] < 0:
#         if max_days_one > max_days_two:
#             max_days_two = max_days_one
#             max_days_one = 0
#         else:
#             max_days_one = 0
#     days -= 1
#     count += 1
# if max_days_one > max_days_two:
#     max_days_two = max_days_one
#
# print(f'Максимальное кол-во плюсовых дней подряд {max_days_two}')
