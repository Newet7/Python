a = {1, 2, 3, 5, 8} # одно множество
b = {2, 5, 8, 13, 21} # второе множество
c = a.copy() # c = {1, 2, 3, 5, 8} ------- создать множество на основе имеющегося!
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} ----- объединение множеств "1" +юнион+ "2"


i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

# можно использовать изменяемые множества и неизменяемые!

# работа с неизменяемыми множествами (замороженными)

s = frozenset(a)
