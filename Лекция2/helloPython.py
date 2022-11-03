# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# #data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

#____________________

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

#____________________

# import Ex002 as h
# print(h.f(1))

#____________________

def concatenatio(*params):
    res: int = 0 #res: str = ""
    for item in params:
        res += item
    return res
#print(concatenatio('a', 's', 'd', 'w')) # asdw
#print(concatenatio('a', '1', 'd', '2')) # a1d2
print(concatenatio(1, 2, 3, 4)) # TypeError: ...

