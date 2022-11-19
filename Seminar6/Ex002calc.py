#Задача 2. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий.

#Сделать калькулятор в одну строку!
# 2+2 => 4 25 мин
# 1+2*3 => 7

#A

def sum(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

formula = '22*223'
formula = list(formula)

number = ''
formulaElements = []

for i in formula:
    if i.isdigit():
        number += i
    else:
        formulaElements.append(int(number))
        operator = i
        number = ''
print(formulaElements)
formulaElements.append(int(number))
print(formulaElements)
operations =\
    {
        '+': sum(formulaElements[0], formulaElements[1]),
        '-': formulaElements[0]-formulaElements[1],
        '*': mult(formulaElements[0], formulaElements[1])
    }
print(operations[operator])

def calc():
    formula = '1+20*33/33-7'
    print(formula, '=', eval(formula))
