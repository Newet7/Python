# Задача 1. Задайте двумерный массив случайных
# чисел размером 4х5. Случайные числа не должны
# повторяться. Запишите массив в txt-файл.
import random


rows = 4
columns = 5
numbers = [0]*rows #1 эл-т умноженный на rows, превращает в список из 4х нулей
used = [] #список использованных чисел

for i in range(len(numbers)): #
    numbers[i] = list(None for _ in range(columns))  #каждый ноль превратили в строку из нулей 
    #random.randint(0, 100) вместо 0 решение с рандомными числами, но повторяющимися...
print(numbers)

for i in range(rows):
    for j in range(columns): #пробегаемся по всем индексам (по строке и столбцу)
        current_numbers = random.randint(0,30) # генерируем случайное число
        while current_numbers in used: # если число уже есть в списке чисел, мы генерируем новое
            current_numbers = random.randint(0,30) # до тех пор пока не найдём нужное значение
        numbers[i][j] = current_numbers
        used.append(current_numbers)

# print(numbers[0][3])
for row in numbers:
    print(row)

