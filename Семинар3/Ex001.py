#Задача 0. Создайте скрипт func и функцию чтения последней
# строки файла. Вызовите её из скрипта example.

# data = open('text.txt', encoding='utf-8')
# print(data)
# #print(data.readlines()) #['РњРѕСЂРѕР· Рё СЃРѕР»РЅС†Рµ\n', 'РґРµРЅСЊ С‡СѓРґРµСЃРЅС‹Р№'] - карявый вывод, замена кодировки , #кодировка текста изночальна utf-8, а тут кодировка (encoding='cp1251'), в итоге при раскодировке в 2 раза больше символов.
# # можем в директиве open добавить кодировку нужного нам формата!

# text = data.readlines()
# print(text[-1]) #text[len(text) -1]

# data.close()

import example

example.ReadLastRow()