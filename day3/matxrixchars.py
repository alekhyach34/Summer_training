'''i/p: 3
     abc
     qwr
     xnv
     "awvarnbrv" o/p:yes
     "awvaxbrv"  o/p:no
n=int(input())
s=input()
m = []
for i in range(n):
    m.append(input())
for i in range(len(s)):
        if s[i] not in m[i%n]:
            print("no")
            break
else:
    print("yes")
'''
n=int(input())
s=input()
m = []
f=0
for i in range(n):
    m.append(list(input()))
for i in range(len(s)):
        if s[i] in m[i%n]:
            print("no")
            f=1
            break
        else:
            m[i].remove(s[i])
if (f==0):
    print("yes")
