#Задача 4. Дан список, выведите его первый и последний элементы.

import random

size = 10

numbers = [random.randint(1,10) for i in range(size)]
print(numbers)
print(numbers[0], numbers[-1])






