#Задача 2. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять 
# количество вхождений 
# одной строки в другую.

#«qwe» «qwertyqwe» -> 2 




string_1 = input()
string_2 = input()
count=0

if len(string_1) > len(string_2):
    print(string_1)
    for i in range(len(string_1)):
        #print(string_1[i: i+len(string_2)])
        # if string_1 == string_2[i; 3]
        # i+=
        if string_2 == string_1[i: i+len(string_2)]:
            count +=1
    print("колличество совпадений строк" , count)


#Решение 2

# symbols = "qwe"
# phrase = "qwertyqwe"
# count = 0
# lenSymbols = len(symbols)
# lenPrase = len(phrase)
# r = range(0, lenPrase-2)
# for i in r:
#     if symbols == phrase[i: i + lenSymbols]:
#         count += 1
# print(count)

#решение3 с помощью метода count

# str1 = input('Enter text1: ')
# str2 = input('Enter text2: ')
# print(f'Text1 include Text2{str1.count(str2)} time(s)')
