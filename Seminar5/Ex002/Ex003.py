#Задача 2. В зоопарк отправили отчёт о новом поступлении зверей 
# с ошибкой, в результате которой некоторые данные не расшифровались. 
# Расшифруйте данные. Определите, в какой клетке находится лев. 
# Номер клетки совпадает с номером строки.

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def ConverToBinary(number):
    result =''
    while number>0:
        result = str(number%2)+result
        number = number//2
    return result

codeList = [ConverToBinary(i) for i in range(len(alphabet))]
# print(codeList)
# codeList = [ConverToBinary(i) for i in codeList]
# print(codeList)
codeList = ['0'*(6-len(i))+i for i in codeList]
# print(codeList)

dictionary = {}
for i in range(len(codeList)):
    dictionary[codeList[i]] = alphabet[i]
print(dictionary)

#считать файл

data = open('animals.txt', 'r')
animalCodeList = data.readlines()
data.close()

for animal in animalCodeList:
    for i in range(len(animal)//6):
        bias=i*6
        print(dictionary[animal[bias:bias+6]], end='')
    print()


