# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


n = int(input('Введите число n: '))
my_list = []
sum = int(0)
for x in range (1, n+1):
    ind = round((1 + 1 / x)**x, 2)
    my_list.append(ind)
    sum += my_list[x-1]
print(my_list)
print(sum)
