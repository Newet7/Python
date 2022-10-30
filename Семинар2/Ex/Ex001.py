# Задача 0. Дано число N. Найти все его делители. Для
# каждого делителя укажите чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный),
# 1(нечётный) 

# def Zadacha0():
#     number = 60
#     for i in range(1, number+1):
#         if number % i == 0:
#             print(i, end = ' ')
#             if i % 2 == 0:
#                 print( '- четный') 
#             else:
#                 print('-нечетный')

# Zadacha0() # не забыть вызвать ф-цию

def CheckEven (x):
    if x % 2 == 0:
        return '- четный'
    else:
        return '-нечетный'

def Zadacha0(y):
    for i in range(1, y+1):
        if y % i == 0:
            print(i, end = ' ')
            print(CheckEven(i))

number = 60

Zadacha0(number) # не забыть вызвать ф-цию