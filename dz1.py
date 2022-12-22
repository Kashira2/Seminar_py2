# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num1 = float(input('Введите число: '))
num1 = str(num1)
num1 = num1.split('.')

num2 = str(num1[0]) + str(num1[1])
num2 = int(num2)
sum = int(0)
while num2 // 10 > 0:
    sum += num2 % 10
    num2 = num2 // 10

print(sum + (num2 % 10))

#from decimal import Decimal

# temp = num1[delete]
# num1[delete] = num1[len(num1) - 1]
# num1[len(num1) - 1] = temp

# while num1 % 1 != 0:
#     num1 = num1 * 10 
# print(Decimal(num1))
# print(num1)

