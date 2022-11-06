#Задача 3. Сгенерируйте список случайных чисел от 1 до 20, 
# состоящий из 10 элементов. 
# Удалите из списка дубликаты уже имеющихся элементов.


import random

def GetNumbers():
    data = open('list.txt', 'w')
    numbers = [random.randint(1,20) for i in range(0, 10)]
    data.write(str(numbers))
    #print(numbers)
    data.close()
    return numbers

#___________решение задачи из файла со списком, удаляем все дубликаты, запитые и тд.

def FinderDublicateList():
    data = open('list.txt', 'r', encoding='utf-8')
    num = data.readline()[1:-1].split(', ')
    num = [int(i) for i in num]
    num = set(num)
    print(type(num), num)
FinderDublicateList()

#________________ решение задачи без файла со списком, просто в терминале
#print(GetNumbers()) 
data = open('list.txt', encoding='utf-8')
num = data.readlines()
data.close()
print(set(num))
#print(set(GetNumbers()))

print(list(set(list(random.randint(1, 20) for _ in range(10)))))




