def isprime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:    #line2
            return 0
    return 1
def prime(n,m):
    for i in range(m-1,n,-1):   #line3
        if (isprime(i)):
            return i
    return 0           #line 4
a=[4,8,14,22,36,68]
s=0
for i in range(0,len(a)-1):
     s=s+isprime(a[i],a[i+1]) #line1
print(s)