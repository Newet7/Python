# практическое задание__________ выполнил сам

# list = [1, 2, 3, 5, 8, 15, 23, 38]
# def f(x):
#     return x**2
# list = [(i, f(i)) for i in list if(i%2==0)]
# print(list)

# из лекции_________________________

# def select(f, col):
#     return [f(x) for x in col]

# def where(f,col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)

# print(res)

#________________ map()

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x+10, li)) #map object at 0x000000DA7E6FB5B0> -- поэтому надо обернуть в list()
# print(li)

# ________________ решаем задачу

# data = list(map(int, input().split())) 
# print(data)
# технически можно неделать list() а сразу пробежаться по файлу
# data = list(map(int, input().split()))

# for e in data:
#     print(e)

# print('--')

# for e in data: #без list() не даёт дважды по map() пробежаться
#     print(e)

#_______________________ финал нашего первого варианта, добавляем map()

# def select(f, col):
#     return [f(x) for x in col]

def where(f,col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)