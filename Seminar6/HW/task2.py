# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве 
# последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

size = [0, 5, 6, 2, 7, 7, 8, 1, 1, 9]
# numbers = [random.randint(1,10) for i in range(size)]
# print(numbers)
N = int(input("Введите трехзначное число n: "))
Nlist = list(str(N))
N1 = int(Nlist[0])
N2 = int(Nlist[1])
N3 = int(Nlist[2])

# index1 = size.index(N1)
# index2 = size.index(N2)
# index3 = size.index(N2)

for i in range(len(size)):
    if size[i] == N1:
        if size[i+1] == N2:
            if size[i+2] == N3:
                print('yes')
            else:
                print('no')
#или

allNumbers = ''
for i in size:
    allNumbers = allNumbers + str(i)

print('да' if allNumbers.count(str(N))> 0 else 'нет')







