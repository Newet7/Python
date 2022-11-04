#Задача 4. Считайте строковые данные из файла. 
# Создайте словарь, содержащий все символы в файле.

data = open('text.txt', encoding='utf-8')
string1 = data.read()
data.close()
new_dictionary = {}
print(string1)
for i in string1:
    new_dictionary[i] = i #индексы в словарях являются ключами
print(new_dictionary)
