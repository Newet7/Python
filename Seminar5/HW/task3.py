# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]



from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

# list_numbers = [1, 2, 2, 5, 5, 7, 4, 2, 1]
# print(list_numbers.count(2))



origin = create_list(size, m, n)
element_count = len([item for item in origin if item != 0])

counter = {}
 
for elem in origin:
    counter[elem] = counter.get(elem, 0) + 1
 
doubles = [count for element, count in counter.items() if count > 1]
print(sum(doubles))

#print(max(set(origin ), key=lambda x: origin.count(x)))
print(origin)
print(get_unic_value(origin))


