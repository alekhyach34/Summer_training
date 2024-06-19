
def fun(l1,l2,l3):
    for i in l1:
        for j in l2:
            if i%2==0 and j%2!=0:
                l3.append(i+j)
    return l3
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
l3=[]
print(fun(l1,l2,l3))
