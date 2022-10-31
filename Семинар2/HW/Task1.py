#Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))

def factorial_list(n):
    factorial = 1
    factorials = []
    for i in range(1, n+1):
        factorial *= i
        factorials.append(factorial)
    return factorials

print(factorial_list(N))