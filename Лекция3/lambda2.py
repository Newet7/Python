# def sum(x,y):
#     return x+y
#sum = lambda x,y: x+y

def mylt(x,y):
    return x*y

def calc(op, a, b):
    print(op(a,b))

calc(mylt,4,5)

# f = sum
# calc(f,4,5)

#calc(sum, 4,5) или вместо sum и calc написать одной строкой -->
calc(lambda x,y: x+y, 4,5)
