#Задача 1. Дан файл, заполненный числами построчно. Считайте файл. 
# Выведите все элементы, стоящие на чётных строках, а потом на нечётных.


def Number():
    num = open('text.txt', encoding='utf-8')
    #print(num)
    point = num.readlines()
    num.close()
    # for i in range(len(point)):  
    #     if (i%2 == 0):
    for i in range(0,len(point),2): 
            print(point[i], end='') 
    print()
    # for i in range(len(point)):  
    #     if (i%2 != 0):
    for i in range(1,len(point),2): 
            print(point[i], end='') 
Number()
