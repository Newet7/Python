path = '/Users/рп/Desktop/учёба/GeekBrains/1 четверть/Python/Лекция3/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '': #пробегаемся по всей нашей строке, с проверкой "пока моя строка не пустая"
    space_pos = data.index(' ') #найти первую позицию пробела
    numbers.append(int(data[:space_pos])) # взять всё что от первого символа до пробела, превратить в число, и добавить в список номеров
    data = data[space_pos+1:]
out = [] # новый список
for e in numbers: # пробегаемся по исходному
    if not e % 2: # число четное
        out.append((e,e **2)) # добавляем в список кортеж, число + число в квадрате.
print(out)