# list=[]

# for i in range(1, 101):
#     #if(i%2 == 0):
#     list.append(i)

# print(list)


list=[i for i in range(1,21) if(i%2 == 0)] # cписок
list2=[(i, i) for i in range(1,21) if(i%2 == 0)] # список кортежей

print(list)
print(list2)

# или обработка

def f(x):
    return x**3

list3=[(i, f(i)) for i in range(1,21) if(i%2 == 0)] # возводим чётные числа в 3 степень, или подключим кортежи
print(list3)  
