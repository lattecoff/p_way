# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randrange

# инициализируем данные.
max_elem = 0
my_list = list()

# вводим размемры списка.
list_size_row = int(input("Введите количество строк матрицы: "))
list_size_coll = int(input("Введите количество столбцов матрицы: "))

# создаем матрицу и заполняем случайными числами.
for row in range(list_size_row):
    my_list.append([randrange(0, 100) for i in range(list_size_coll)])

# выводим полученную матрицу на экран.
for i in range(list_size_row):
    print(my_list[i])

for i in range(list_size_row -1):
    if (my_list[i][i]) > (my_list[i + 1][i + 1]):
        max_elem = my_list[i][i]
    else:
        max_elem = my_list[i + 1][i + 1]

print(max_elem)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
