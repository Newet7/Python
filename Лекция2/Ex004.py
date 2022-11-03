# Множества

colors = {'red', 'green', 'blue'}

print(colors) # {'red', 'green', 'blue'}
colors.add('red') # можно элементы добавлять!
print(colors) # {'red', 'green', 'blue'} ----- добавили такое-же, соответственно оно не появилось!
colors.add('gray') # добавили опять
print(colors) # {'red', 'green', 'blue','gray'} ----- оно отличаетсяЮ значит добавилось!
colors.remove('red') # ф-ция ремув удалить какойто элемент!
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' - если удалить несуществующий элемент то будет ошибка.
colors.discard('red') # ok - удалить без вызова ошибки , если такого элемента НЕТ!
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } - ---- очистить множество, и дальше работать с пустым множеством.
print(colors) # set()