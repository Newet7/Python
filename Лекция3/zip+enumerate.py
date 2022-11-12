user = ['user1','user2','user3','user4','user4']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(user,ids, salary)) # пробигается по минимальному списку, ответ будет исходя из самого минимального списка по кол-ву элементов
print(data)

data = list(enumerate(user)) # нумирация
print(data)