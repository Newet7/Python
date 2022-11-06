#Задача 2. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». 
# На главную роль нужен актёр обладающий всеми тремя качествами. 
# Определите, сколько есть претендентов на главную роль. 
# Списки актёров поместите в соответствующие файлы.

# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад

# handsome = set()
# smart = set()
# strong = set()

# with open('handsome.txt', encoding='utf=8') as inf:
#     for line in inf.readlines():
#         handsome.add(line.rstrip())
# print(handsome)

# with open('smart.txt', encoding='utf=8') as inf:
#     for line in inf.readlines():
#         smart.add(line.rstrip())
# print(smart)

# with open('strong.txt', encoding='utf=8') as inf:
#     for line in inf.readlines():
#         strong.add(line.rstrip())
# print(strong)

# print(*(handsome&smart&strong), sep='\n')

def openFile(nameFile): #метод открывашки файла по имени
    f = open(nameFile, encoding='utf-8') #открываем файл
    phrase = f.readlines() # считываем данные
    f.close() # закрываем файл
    list = phrase[0].split() # считываем 1 строку и разюиваем методом split
    return set(list) # возвращаем в множество

handsome = openFile('handsome.txt')
smart = openFile('smart.txt')
strong = openFile('strong.txt')

print(handsome.intersection(smart).intersection(strong)) # расспечатываем пересечения, сначала первого со вторым - следом идёт проверка результата с третьим списком множества
