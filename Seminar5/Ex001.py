# Задача 1. На вход подаётся четырёхзначное число. 
# Получите список, состоящий из цифр 
# данного числа, увеличенных на 10.
# 9650 - [19, 16, 15, 10]

import numbers

N = list(input())
print(N)
N = map(int, N)
res = list(map(lambda x: x+10, N))
print(res)
