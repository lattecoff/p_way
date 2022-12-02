# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from random import randrange

lenght = 10
mean = 0;

my_list = [randrange(0, 100) for i in range(lenght)]

mean = sum(my_list) / len(my_list)

for i in my_list:
    if i < mean:
        print(i)