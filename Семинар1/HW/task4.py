# Задача 4. Напишите программу, которая на вход принимает число (N),
#  а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

#n=int(input('enter starting range'))
m=int(input('enter ending range'))
even_in_range=[i for i in range(1,m+1) if i%2==0 ]
print(even_in_range)



# def print_even_numbers(start, stop):
#     for i in range(0,11):
#         if i % 2 == 0:
#             print (i)
 
# print(print_even_numbers(10,20))
