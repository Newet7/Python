# Задача 3. В двумерном массиве хранятся средние дневные 
# температуры с мая по сентябрь за прошлый год. Каждому 
# месяцу соответствует своя строка. Определите самый жаркий 
# и самый холодный 7-дневный промежуток этого периода. 
# Выведите его даты.
import random

rows = 5
columns = 30
numbers = [0]*rows #1 эл-т умноженный на rows, превращает в список из 4х нулей
used = [] #список использованных чисел

for i in range(len(numbers)): #
    numbers[i] = list(random.randint(10, 40) for _ in range(columns))
print(numbers)