# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
# 60 -> 2, 2, 3, 5

import math

number=int(input('Введите число: '))
list =[]

for i in range(2, int(math.sqrt(number)) + 1): # находим квадратный корень, обычно делитель не будет больше корня
    while (number % i == 0): # while, а не if
        list.append(i)
        #print(i)
        number //= i # целочисленное деление, убираем множитель из числа
if (number != 1): # но один делитель может быть больше корня
    print (number)

print(list)


