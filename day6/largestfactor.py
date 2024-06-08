n = int(input())
k = int(input())
l=[]
a=n//k
for i in range(1, 12):
    if n % i == 0:
        l.append(i)
if a in l:
    print(a)
