#5. Напишите программу, которая находит наибольшее
#  и наименьшее число из списка значений

# numbers = [int(el) for el in input().split()]
# max_el = min_el = numbers[0]
# for number in numbers:
#     if number > max_el:
#         max_el = number
#     elif number < min_el:
#         min_el=number
# print(f'max={max_el}')
# print(f'min={min_el}')

#- - - - - - -- - - -
# решение стандартными методами Python

numbers = [int(el) for el in input().split()]
print(f'max = {max(numbers)}')
print(f'min = {min(numbers)}')
