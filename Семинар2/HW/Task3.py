#Задача 3. Даны две строки. Посчитайте сколько раз 
# каждый символ первой строки встречается во второй
#«one» «onetwonine» - o – 2, n – 3, e – 2

#char = input()

chars = "one"
check_string = "onetwonine"

for char in chars:
  count = check_string.count(char)
  if count > 1:
    print (char, count)




# string_1 = input()
# string_2 = input()
# count=0

# if len(string_1) > len(string_2):
#     print(string_1)
#     for i in range(len(string_1)):
#         #print(string_1[i: i+len(string_2)])
#         # if string_1 == string_2[i; 3]
#         # i+=
#         if string_2 == string_1[i: i+1]:
#             count +=1
#     print("колличество совпадений букв" , count)

#решение3 с помощью метода count

# str1 = input('Enter text1: ')
# str2 = input('Enter text2: ')
# print(f'Text1 include Text2{str1.count(str2)} time(s)')