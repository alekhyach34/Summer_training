a= int(input()) #12
b = int(input()) #15
'''for i in range(2, (min(a,b)//2) + 1):
    if a % i == 0 and b % i == 0:
        print("not co prime")
        break
    else:
        print("co prime")'''
import math
a=math.gcd(a,b)
if a==1:
    print('coprime')
else:
    print("not co prime")
