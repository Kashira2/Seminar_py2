####################################  Напишите программу,
# ################################### которая принимает на вход число N и выдаёт последовательность из N членов.

# num1 = int(input('Введите число: '))

# for degree in range(num1):
#     print((-3)**degree, end =' ')


# my_list = []                    то как добавлять в список
# my_list.append(3)

################################# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# num1 = int(input('Введите число: '))


# if num1 > 0:
#     for i in range(-num1, num1+1):
#             if i == num1:
#                 print(i, end = ' ')
#             else:
#                 print(i, end = ', ')
# elif num1 < 0:
#     for i in range(num1, -num1+1):
#             if i == num1:
#                 print(i, end = ' ')
#             else:
#                 print(i, end = ', ')

########################################## через лист

# num1 = int(input('Введите число: '))

# my_list = []

# for i in range(-num1, num1+1):
#     my_list.append(i)

# print(*my_list, sep =', ')

#########################################   УСЛОЖНЕННАЯ


# num1 = int(input('Введите число: '))

# my_list = []

# for i in range(-num1, num1+abs(num1)//num1, abs(num1)//num1):
#     my_list.append(i)

# print(*my_list, sep =', ')


################################################
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# num1 = float(input('Введите число: '))

# if int(num1) == num1:
#     print('Нет дробной части')  
# else:   
#     print(int(abs(num1) * 10) % 10) 

#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ через строку

# num1 = input('Введите число: ')

# num1 = num1.split('.')
# if len(num1)>1:
#     print(num1[1][0])
# else:
#     print('Нет дробной части')

##################### про Decimal

# from decimal import Decimal

# num1D = Decimal('0.567899')
# num1 = 0.567899

# print(num1D * 10)
# print(num1 * 10)

#############################