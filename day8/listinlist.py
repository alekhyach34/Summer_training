#a=[1,2,3,4,1,2,3,1,2]# o/p:[[1,2,3,4],[1,2,3],[1,2]]
#a=[2,3,1,3,4,3,2] # o/p:[[2, 3, 1,4], [3, 4], [3, 2]]
#a=[4,5,2,1] o/p:[[4,5,2,1]]
#a = list(map(int,input().split()))
'''def sublists(lst):
    l = []
    l1 = []
    for i in lst:
        if i not in l1:
            l1.append(i)
        else: 
            l.append(l1)
            l1 = [i]
    l.append(l1)
    return l
a=[2,3,1,3,4,3,2]
result=sublists(a)
print(result)'''
'''ip1:[1,2,3,4,1,2,3,1,2]
op1:[[1 2 3 4],[1 2 3],[1 2]]
ip2:[2,3,1,3,4,3,2]
op2:[[2 3 1 4],[3,2],[3]]
ip3:[4,5,2,1]
op3:[[4,5,2,1]]'''
#a=list(map(int,input().split(",")))
a=[2,3,1,3,4,3,2]
l1=[]
c=0
while(c!=len(a)):
    l2=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in l2):
                c+=1
                l2.append(a[i])
                a[i]='a'
    l1.append(l2)
print(l1)
#using DICTIONARIES
a=list(map(int,input().split(",")))
d={}
l1=[]
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i+1]
c=0
while(c!=len(a)):
    l2=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            l2.append(i)
    l1.append(l2)
print(l1)