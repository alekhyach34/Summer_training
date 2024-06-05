def rev(n, temp):  
    if (n == 0):
        return temp
    return rev(n // 10,(temp * 10) + (n % 10))
n = int(input()) 
temp = rev(n, 0)
if (temp == n): 
	print("yes")
else:
	print("no")
