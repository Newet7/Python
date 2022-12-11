#Задача 2. Считайте двумерный массив из файла.
# Найдите разницу между вторым максимальным и
# вторым минимальным элементами массива.

import random

def printMatrix(numbers):
    for row in numbers:
        print(row)

def zadacha0():
    rows = 4
    columns = 5
    numbers = [0]*rows #1 эл-т умноженный на rows, превращает в список из 4х нулей
    used = [] #список использованных чисел
    for i in range(len(numbers)): #
        numbers[i] = list(None for _ in range(columns))
    for i in range(rows):
        for j in range(columns): #пробегаемся по всем индексам (по строке и столбцу)
            current_numbers = random.randint(0,30) # генерируем случайное число
            while current_numbers in used: # если число уже есть в списке чисел, мы генерируем новое
                current_numbers = random.randint(0,30) # до тех пор пока не найдём нужное значение
            numbers[i][j] = current_numbers
            used.append(current_numbers)
    return numbers

def zadacha2():
    numbers = zadacha0()
    printMatrix(numbers)

    result = []
     
    for row in numbers:
        for el in row:
            result.append(el)
    print(result)
    result = list(set(result)) #сортировка от меньшего к большему
    #result.sort()
    print(result)
    print(result[1], result[-2])
    print(f'{result[-2]} - {result[1]} = {result[-2] - result[1]}')




print(zadacha2())


