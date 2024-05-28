'''def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num
def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num
def output_number(num):
    if is_prime(num):
        return num
    else:
        return next_prime(num)
num=int(input())
print(output_number(num))
'''
num=int(input())
while(1):
    c=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            c+=1
            break
    if c==0:
        print(num)
        break
    else:
        num+=1

