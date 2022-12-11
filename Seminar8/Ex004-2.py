# Задача 4. Дан двумерный массив. Определите
# номер строки и столбца, в котором находится
# максимальный элемент.


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
    print(f'{result[-2]} - {result[1]} = {result[-2] - result[1]}')


def zadacha4():
    numbers = zadacha0()
    printMatrix(numbers)
    result = []
        
    for row in numbers:
        for el in row:
            result.append(el)
    print(result)

    max1 = max(result)
    print(f'максимум равен {max1}')
    max_index = result.index(max1)
    print(f'его индекс равен {max_index}')

    rows = len(numbers)
    columns = len(numbers[0])
    print(max_index//columns+1)
    print(max_index%columns+1)

zadacha4()


