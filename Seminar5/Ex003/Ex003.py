#Задача 3. Имеется информация о том, телефонами каких компаний сейчас 
# торгуют магазины. Определите те компании, 
# чьи телефоны присутствуют в каждом магазине.

data = open('Телефоны.txt', 'r')
phones = data.readlines()
data.close()


shopF = set(phones[1].replace('\n', '').split(', '))  #строки можно разбить split(), заменим \n на пустой символ replace()
shopS = set(phones[3].replace('\n', '').split(', ')) 
shopT = set(phones[5].split(', ')) 

# найти пересечения intersection()
print(shopF.intersection(shopS).intersection(shopT))
# print(shopS)
# print(shopT)