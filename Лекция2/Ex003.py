dictionary = {}
dictionary = \
    {
    'up': '↑',
    'left': '←',
    'down': '↓',
    'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)


for k in dictionary.values():
    print(k)