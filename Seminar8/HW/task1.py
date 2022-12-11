# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.


import random


group = 3
students = 25
numbers = [0]*group 
used = [] 
for i in range(len(numbers)): #
    numbers[i] = list(None for _ in range(students))

for i in range(group):
    for j in range(students):
        current_numbers = random.randint(1,5)
        numbers[i][j] = current_numbers
        used.append(current_numbers)
for row in numbers:
    print(row)

result = []
     
for row in numbers:
    for el in row:
        result.append(el)
print(result)

a = sum(result[0:24]) / len(result[0:24])
b = sum(result[25:49]) / len(result[25:49])
c = sum(result[50:74]) / len(result[50:74])

print(a, b, c)

if a > b:
    print(f'наилучший средний бал из 3х групп у группы 1, ср бал {a}') if a > c else print(f'наилучший средний бал из 3х групп у группы 3, ср бал {c}')
else:
    print(f'наилучший средний бал из 3х групп у группы 2, ср бал {b}') if b > c else print(f'наилучший средний бал из 3х групп у группы 3, ср бал {c}')


# middle_score = sum(rows) / len(list_scores)

 
