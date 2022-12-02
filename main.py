# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from random import randrange

lenght = 100
sum = 0;

my_list = [randrange(-100, 100) for i in range(lenght)]

for i in my_list:
    if i > 0 and i %2 == 0:
        sum += i
        
print(sum)