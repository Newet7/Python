#Задача 2. В зоопарк отправили отчёт о новом поступлении зверей 
# с ошибкой, в результате которой некоторые данные не расшифровались. 
# Расшифруйте данные. Определите, в какой клетке находится лев. 
# Номер клетки совпадает с номером строки.

from functools import reduce

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

with open('animals.txt') as inf:
    for line in inf.readlines(): #каждую строку считываю
        numbers = line.rstrip()
        chars = [numbers [i:i+6] for i in range(0, len(numbers), 6)] # массив(двоичная кодировка) каждой буквы
        print(chars)
        for char in chars:
            i = int(char, 2) # двоичную в десятичную
            print(alphabet[i], end='') # и выводим букву, окончание строки
        print() # перенос для норм чтения
