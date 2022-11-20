# sum = lambda a, b: a + b

# x = int(input('x = '))
# y = int(input('y = '))

# print(f'сумма {x} + {y} = {sum(x,y)}')

#как модернизировать код?



x = 0
y = 0
def init(a,b):
    global x
    global y
    x = a 
    y = b

def sum():
    return x + y
