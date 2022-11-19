#Задача 1. Даны два случайных пятизначных числа.
#  Определить, состоят ли они из одних и тех же цифр.
#72426, 27624 –> да 44444, 44441 -> нет
import random

def Zadacha0():
    size = 4
    numbers = [random.randint(1,10) for i in range(size)]
    print(numbers)
    print('yes' if len(numbers) == len(set(numbers)) else 'no')

#проверить на 5значность
def CheckNum(number):
    return 10000 <= number <= 99999

def CountAllnum(number):
    number = str(number)
    number = set((i, number.count(i)) for i in set(number))
    print(number)
    return number
def zadacha1():
    num1 = 55234
    num2 = 23455

    # print(set(str(num1)))
    # print(set(str(num2)))

    if CheckNum(num1) and CheckNum(num2):
        # делаем список из кортежей
        num1 = CountAllnum(num1)
        num2 = CountAllnum(num2)

        print('yes' if num1 == num2 else 'no')
        # if set(str(num1))==set(str(num2)):
        #     print('совпадают')
        # else:
        #     print('различны')
    else:
        print('числа не удовлитворяют условию')

    

zadacha1()