# Задача 3. В зрительном зале 25 рядов, в каждом из которых 36 мест.
# Информация о проданных билетах должна храниться в виде
# двумерного массива, в котором номера строк соответствуют номерам
# рядов, а номера столбцов – номерам мест.
# Определите, где лучше сесть компании из M человек, если они хотят
# ряды только с K-го по N-ный.

# Все люди должны быть рядом после посадки.
# Если это невозможно, вывести соответствующее сообщение.
import random
import numpy as np #требуется подключить numpy

seats = random.randint(2, size=(25, 36))

print(seats)

M = int(input('how many people: '))
K = int(input('the closert row: '))
N = int(input('the farthest row: '))
found = False

for i in range(K, N+1):
    for j in range(36-M+1): #место в ряду, минус кол-во людей...
        if 1 not in seats [i, j: j+M+1]:
            print(seats[i,j: j+M])
            print(i+1, j+1)
            found = True
        if found:
            break
    if found:
        break
else:
    print('no seats =(')