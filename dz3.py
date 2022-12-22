# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

# import random
# print(random.randint(0,100))

from random import randint as RI

num1 = int(input('Задайте размер списка: '))
my_list = []

for i in range(num1):
    my_list.append(RI(0,100))
print(my_list)

for i in range(0, num1, 2):
    if my_list[i] != my_list[len(my_list)-1]:    
        temp = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = temp
    else:
        temp = my_list[i]
        my_list[i] = my_list[0]
        my_list[0] = temp

print(my_list)