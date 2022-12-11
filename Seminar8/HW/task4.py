# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
# Вопрос и правильный ответ сохраните в файл. 
# Реализуйте алгоритм шифрования правильного ответа.

questions = [{'question': 'Самая большая страна в мире?',
              'answer': 'РОССИЯ'},
             {'question': 'Самое теплое время года в России?',
              'answer': 'ЛЕТО'}]
q = int(input('Введите номер вопроса: '))
d = {}
b = {}
x = []
s = ''
i = 0
 
d = questions[q - 1]
answer = d['answer']
 
print('Вопрос:', d['question'])
print('Ответ:', 'x' * len(answer))
 
while i < len(answer):
    x.append('x')
    i += 1
while s != answer:
    symbol = input('Введите букву: ').upper()
    for i in range(len(answer)):
        if symbol != answer[i]:
            flag = False
        elif symbol == answer[i]:
            if answer[i] in b:
                b[answer[i]].append(i)
            else:
                b[answer[i]] = [i]
    for j in b:
        for k in b[j]:
            x[k] = j
    for l in range(len(x)):
        if x[l] != 'x':
            s += x[l]
    print(s)
    print(x)

    