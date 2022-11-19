import random

size = 4

numbers = [random.randint(1,10) for i in range(size)]
print(numbers)

print('yes' if len(numbers) == len(set(numbers)) else 'no')