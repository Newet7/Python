# Задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
# 60 -> 2, 2, 3, 5


number=int(input('Введите число: '))

def FindDiviger(number):
    divigers = []
    for i in range(2, number//2):
        while (number%i==0):
            if number % i == 0:
                divigers.append(i)
                number /= i
    print(divigers) 

FindDiviger(number)