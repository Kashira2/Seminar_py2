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
