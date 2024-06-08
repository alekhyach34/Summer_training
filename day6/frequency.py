#i/p=[4,8,2,4,4,8,4] o/p:4-->it is occuring more times than the length of the list
#w!=current c=c-1  #only when c=0 update w
l=list(map(int, input().split()))
c=1
w=l[0]
for i in range(1,len(l)):
    if l[i] == w :
        c+=1
    else:
        c-=1
        if c==0:
            c=1
            w=l[i]
print(w)
