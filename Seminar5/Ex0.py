# Задача 0. С помощью анонимной функции найдите в списке 
# на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100.

import random

numbers = [random.randint(1, 100) for i in range(15)]
print(numbers)

#кратно 5
# for i in numbers:
#     if i%5==0:
#         print(i)

result = lambda x: x%5==0
result = list(filter(result, numbers))
print(result)


