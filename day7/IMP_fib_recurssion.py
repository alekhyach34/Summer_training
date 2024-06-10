def fib(n):
    for i in range(1,10):
        print(fib(n),end=" ")
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
n=5
print(fib(n))

