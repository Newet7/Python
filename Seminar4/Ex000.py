import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))
print(numbers)

data = open('numbers.txt', 'w')
data.writelines(str(numbers))
data.close()