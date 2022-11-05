# Задача 3. Напишите скрипт генератора паролей
# заданной длины, состоящих из букв и чисел.
# Создайте скрипт для сохранения пароля в файл
# password.txt.

#из таблицы символов брать символы,

import string
from random import randrange as rr


def generate_password(length, code):
    used = [False, False, False]
    pswd = ' '
    while False in used:
        i = rr(len(used))
        if used[i] == True:
            continue
        used[i] = True
        pswd += code[i][rr(len(code[i]))]
    while len(pswd) < length:
        i = rr(len(code))
        pswd += str(code[i][rr(len(code[i]))])
    return pswd

def generate_passwords(count, length, encode): #не повтаряются пороли!
    used_passwords = set()
    for _ in range(count):
        used_passwords.add(generate_password(length, encode))
    return used_passwords

def create_code():  #таблица кодировки, все символы(список)
    avoid_code = 'II1oOO'
    possible_alpha = list() 
    possible_alpha.append([el for el in string.ascii_uppercase if el not in avoid_code])
    possible_alpha.append([el for el in string.ascii_lowercase if el not in avoid_code])
    possible_alpha.append([el for el in string.digits if el not in avoid_code])
    return possible_alpha

def create_file_pswd(psswrds:list):
    with open('password':'w') as ouf:
        for password in psswrds:
            ouf.write(str(password)+'\n')

def main():
    code = create_code()
    n, m = int(input()), int(input())
    passwords = generate_passwords(n, m, code)
    create_file_pswd(passwords)

if _name_ == '_main_':
    main()


