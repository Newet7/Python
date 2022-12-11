# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк 
# превосходит сумму главной диагонали матрицы.
import random

rows = 4
columns = 4
numbers = [0]*rows #1 эл-т умноженный на rows, превращает в список из 4х нулей
used = [] #список использованных чисел

for i in range(len(numbers)): #
    numbers[i] = list(random.randint(0, 100) for _ in range(columns))
print(numbers)

sum_1_diagonal = 0
for x in range(0, rows):
    for y in range(0, rows):
       if x == y:
          sum_1_diagonal = sum_1_diagonal + numbers[x][y]
          print(sum_1_diagonal)
print(sum_1_diagonal)


