
a=input()
n=int(input())
s=''
for i in range(n):
    b=input()
    if b[0]=='L':
        s=s+a[int(b[2])]
    else:
        s=s+a[-int(b[2])]
print(s)
s=list(s)
s.sort()
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()    
    b.append(t)
for i in b:
    if(i==s):
        print("yes")
        break
else:
    print("no")
#using list and append 
a=input()

n=int(input())

s=[]
for i in range(n):
    b=input()
    if b[0]=='L':
        s.append(a[int(b[2])])
    else:        
        s.append(a[-int(b[2])])
s.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))        
    b.append(t)
    for i in b:
        if(i==s):
            print("yes")        
            break
    else:
        print("no")