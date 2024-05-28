a = list(map(int , input().split()))
b= list(map(int , input().split()))
i,j=0,0
c=[]
if(a[i]<b[j]):
    c.append(a[i])
    i=i+1
else:
    c.append(b[j])
    j=j+1
if(i<len(a)):
    c.extend(a[i:])
else:
    c.extend(b[j:])
print(c)
