def line():
    print('-' * 100)


list = [1, 1, 2, 0, -1, 3, 4, 4]
numbers = set(list)
print(len(numbers))

line()

second_list = [1, 2, 3, 4, 5, 6, 7]
k = 3
index = 0
while k > 0:
    second_list.append(second_list[0])
    second_list.pop(0)
    k -= 1
print(second_list)

second_list2 = [1, 2, 3, 4, 5, 6, 7]
k = 2
numbers = second_list2[second_list2[len(second_list2) - k] - 1:len(second_list2)]
index = 0
for i in numbers:
    second_list2.insert(index, i)
    second_list2.pop(len(second_list2) - k)
    k -= 1
    index += 1
print(second_list2)

line()

inDict = {
    'I': 'S001',
    'II': 'S002',
    'III': 'S001',
    'IV': 'S005',
    'V': 'S005',
    'VI': 'S009',
    'VII': 'S007'
}
index = 0
individual = inDict.values()
ind_list = []
for i in individual:
    if i in ind_list:
        ind_list.remove(i)
        continue
    else:
        ind_list.append(i)


print(f'Вывод только индивидуальных ключей в словаре: {ind_list}')

line()