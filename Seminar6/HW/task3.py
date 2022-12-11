import math

#Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.

# дробь представляется кортежом-парой (числитель, знаменатель)
 
def gcd(a,b):   # Наибольший общий делитель (алгоритм Евклида)
    while(b>0):
        a,b=b,a%b
    return a
    
def simplify(pair): # сокращение дроби
    g=gcd(pair[0],pair[1])
    return (pair[0]//g,pair[1]//g)
    
n=int(input("n="))
t=[]
for num in range(1,n+1): # цикл по всем числителям 
    for denom in range(num+1,n+1): # цикл по всем знаменателям
        pair=simplify((num,denom)) # очередная дробь
        t.append(pair) # добавим к списку
s=list(set(t)) # устраняем дубликаты - превращаем список во множество
for q in sorted(s,key=lambda x: x[0]/x[1]): # сортируем по величине частного (в виде float)
    print(str(q[0])+"/"+str(q[1])) # печать


result = []
for i in range(2, 12): #j,i i=7, j=1.2.3.4.5.6
    for j in range(1, i):
        if math.gcd(i,j)==1:
        #if i<j and Fraction(i, j):
            result.append(f'{j}/{i}')
print(result)


num = set()
for i in range(1, 11):
    for j in range(2, 12):
        if i < j and Fraction(i, j):
            x = Fraction(f'{i}/{j}')
            num.append(x)
print(num)