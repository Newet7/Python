def f(x):
    return x**2
print(f(2))
print(type(f))
#___________
g = f
print(f(4))
print(g(4))
#_____________
def calc1(x):
    return x+10
print(calc1(10))

def calc2(x):
    return x*10
print(calc2(10))
#____создаём функцию функции, op функция, x число
def math(op,x):
    print(op(x))

math(calc2, 10)
math(calc1,10)



