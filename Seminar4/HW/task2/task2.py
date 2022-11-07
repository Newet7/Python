# Задача 2. В первой строке файла находится информация 
# об ассортименте мороженного, во второй - информация 
# о том, какое мороженное есть на складе.
#  Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

# 1 открываем файл
# 2 сравниваем строки
# 3 Оставляем только строки из первого списка, если их нет во втором

def openFile1str(nameFile): #метод открывашки файла по имени
    f = open(nameFile, encoding='utf-8') #открываем файл
    phrase = f.readlines() # считываем данные
    f.close() # закрываем файл
    list = phrase[0].split() # считываем 1 строку и разбиваем методом split
    return set(list) # возвращаем в множество

def openFile2str(nameFile): #метод открывашки файла по имени
    f = open(nameFile, encoding='utf-8') #открываем файл
    phrase = f.readlines()[1:] # считываем данные со второй строки
    f.close() # закрываем файл
    list = phrase[0].split() # считываем 1 строку и разбиваем методом split
    return set(list) # возвращаем в множество

ice1 = openFile1str('file.txt')
ice2 = openFile2str('file.txt')
print(ice1-ice2)
#print(ice2)



# f = open('file.txt', encoding='utf-8') #открываем файл
# allice = f.readlines() # считываем данные
# f.close() # закрываем файл
# list = allice[0].split() # считываем 1 строку и разбиваем методом split
# print(list)

# f = open('file.txt', encoding='utf-8')
# ice = f.readlines()[1:]
# f.close()
# list2 = ice[0].split()
# print(list2)



# endice = []

# endice(set(list)-set(list2))

