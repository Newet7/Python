#Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.

x = [0, 1]
y = [0, 1]
print("x| y| ¬ X ∨ Y")
for x in range(0 , 2):
    for y in range(0, 2):
        sum = not x or y
        print(f"{x}| {y}| {int (sum)}")