
def is_prime(x):
    if x==1:
        return 1
    if x==2:
        return 0
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if is_prime(i) and is_prime(a-i):
        print('yes')
        break
else:
    print('no')