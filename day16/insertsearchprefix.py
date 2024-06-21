n=int(input())
l=[]
def prefix(l,n):
    x=[]
    c=0 
    for i in l:
        if n in i:
            c=c+1
            x.append("True")
        else:
            x.append("False")
    return c,any(x)
for i in range(n):
    m,n=input().split(' ')
    if m=='1':
        l.append(n)
    elif m=='2':
        if n in l:
            print("True")
        else:
            print("False")
    elif m=='3':
        print(prefix(l,n))
    elif m=='4':
        l.remove(n)
