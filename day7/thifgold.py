#l=[3,2,4,5,6] op:all possible 3 combinations
'''def all_combinations(l, k=3, start=0, l1=[]):
    if len(l1) == k:
        s=sum(l1)
        m=max(s)
        print(m)
        return
    for i in range(start,len(l)):
        all_combinations(l, k, i + 2, l1+[l[i]])
l = [13, 9, 4, 10, 5,7]
m=0
all_combinations(l)'''

'''ip:[13,9,4,10,5,7]
op:30'''
def all_combinations(l, k):
    def fun(l1, start):
        if len(l1) == k:
            return l1, sum(l1)
        ms = 0           #max sum
        mc = []          #max combination
        for i in range(start, len(l)):
            rc, rs = fun(l1 + [l[i]], i + 2)         #rc-result combination     rs-result sum
            if rs > ms:
                ms = rs
                mc = rc
        return mc, ms
    rc, rs = fun([], 0)
    print(rc,rs)
a = [14, 10, 2, 9, 1, 5]
k = len(a)//2
all_combinations(a, k)

l=[13,9,4,10,5,7]
def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
print(fun(l))