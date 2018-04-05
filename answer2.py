# python

def fact(n):
    if n==1 or n==0:
        return n
    else:
        return n* fact(n-1)

n = int(input())

list = [];
for i in range(n):
    list.append(input())
list = sorted(list)

x = input()

y = n
count = 1
n=n-1

for i in range(y):
    id = list.index(x[i])
    list.remove(x[i])
    if id != 0 :
        count = count + (id) * fact(n)
        
    n = n-1

print(count)

