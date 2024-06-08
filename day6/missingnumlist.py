n=int(input())
l=list(map(int, input().split()))
for i in range(len(l)):
    n=n-i
    if n>=0  n not in l:
        print(n)
 
