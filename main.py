# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from random import randrange

lenght = 10
mean = 0;

# Заполняем список положительными случайными числами.
my_list = [randrange(0, 100) for i in range(lenght)]

# Вычислем среднее значение значений списка.
mean = sum(my_list) / len(my_list)

# Находим элемнты которые меньше среднего значения списка.
for i in my_list:
    if i < mean:
        print(i)