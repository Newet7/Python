#Задача 3. Выведите число π с заданной точностью. 
# Точность вводится пользователем в 
# виде натурального числа.3 -> 3.142
# 5 -> 3.14159

from math import pi

d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')