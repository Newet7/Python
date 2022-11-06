#Задача 1. Создайте файл. Запишите в него N первых 
# элементов последовательности Фибоначчи.
#6 –> 1 1 2 3 5 8
#path = 'file.txt'
data = open('file.txt', 'w')

fib1 = 0
fib2 = 1
n = int(input('Введите число: '))

#file = [fib1, fib2]

# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#     print(fib_sum)
#     file.append(fib_sum)
# print(file)
# data.writelines(str(file))

# ________________решение задачи через кортежи
for i in range(n):
    print(fib1)
    data.writelines(str(fib1)+ ', ')
    (fib1, fib2) = (fib2, fib1+fib2)
