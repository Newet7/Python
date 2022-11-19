# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


nums = [1, 5, 2, 3, 4, 6, 1, 7]

# Первый вариант

def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))

# Второй вариант

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(get_up(nums))

#ДЗ________________________________________

import random

size = 15

numbers = [random.randint(1,100) for i in range(size)]
print(numbers) #рандомный список
index = random.randint(0, size -1)
result = [numbers[index]]

while index < size:   # рандомный перебор списка, от первого рандомного элемента к следующему рандомному элементу, рандомно!
    index = random.randint(index+1, size)
    if index < size:
        if numbers[index] > result[-1]:
            result.append(numbers[index])


print(result) # рандомный элемент списка

