#537=5+3+7=15=>1+5=6=>6 is not prime=>537+1=538=>538=5+3+8=16=>1+6=7=>7 is prime=>538+1
'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True
def digit_sum(n):
    return sum(int(digit) for digit in str(n))
def number_to_single_digit(n):
    while n >= 10:
        n = digit_sum(n)
    return n

def result_number(n):
    sumof_digits = digit_sum(n)
    single_digit = number_to_single_digit(sumof_digits)
    if is_prime(single_digit):
        return n
    else:
        return n + 1

number = int(input())
result = result_number(number)
print(result)
'''
def add(n):
    s=0
    while(n):
      s=s+(n%10)
      n=n//10
    return s
def pnp(n):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
def spnp(n):
    if(n<10):
        print(pnp(n))
    else:
        while(1):
            n=add(n)

n=int(input())
m=n
print(pnp(n))

