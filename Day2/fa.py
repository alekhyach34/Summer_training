'''def fa(x):
    if (x==1):
        return 1
    return x*fa(x-1)
print(fa(5))
'''
def asum(n):
    if(n==0):
        return 0
    return n + asum(n-2)
if n%2==0:
    print(asum(n))
else:
    print(asum(n-1))
n=int(input())
print(asum(n))
