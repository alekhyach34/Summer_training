#l=[3,2,4,5,6] op:all possible 3 combinations
def all_combinations(l, k=3, start=0, l1=[]):
    if len(l1) == k:
        print(l1)
        return
    for i in range(start,len(l)):
        all_combinations(l, k, i + 1, l1+[l[i]])
l = [3, 2, 4, 5, 6]
all_combinations(l)