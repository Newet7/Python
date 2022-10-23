# print ('hello world')

# value = None 
# print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# print(a)
# print(b)

# value = 12334
# print(type(value))

# c = 'hello \nworld'
# print(a,'-',b,'-',c)
# print('{}-{}-{}'.format(a,b,c))
# print(f'{a}-{b}-{c}')
# print('{1}-{0}-{2}'.format(a,b,c))


# list = ['1','2','3','hello',1,2,4.5,True]
# print(list)

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a,'+', b,'=', a+b)

# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# a = int(input('a= '))
# b = int(input('b= '))
# if a>b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Жека':
#     print('Ура, это же Жека!')
# elif username == 'Марина':
#     print('Я так ждала вас Марина')
# elif username == 'Ильнар':
#     print('Ильнар-топ')
# else:
#     print('Привет,', username)


orig = 23
inverted = 0
while orig != 0:
    inverted = inverted * 10+(orig % 10)
    orig //= 10
print(orig)    # не понял что это?