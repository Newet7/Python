# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

N = 132

N = int(input("Введите число n: "))

temp = ''

NN = temp + str(N) +str(N)

NNN = temp + str(N) + str(N) + str(N)

comp = N + int(NN) + int(NNN)
print(f"Результат {N} + {NN} + {NNN} равен:", comp)


