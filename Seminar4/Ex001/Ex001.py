#Задача 1. Создайте кортеж, заполненный случайными числами. 
# Напишите метод, который заменяет 
# элемент в кортеже по заданному индексу.

import random

def chenge_index(numbers, index):
    numbers = list(numbers)
    numbers[index-1] = random.randint(10, 100)
    numbers = tuple(numbers)
    return numbers

size = random.randint(5,12)
numbers = tuple(random.randint(10,100) for i in range(size))
print(numbers)

index =int(input("Введите индекс, который необходимо заменить: "))

print(chenge_index(numbers, index))
