'''
i/p: asd123!@#
o/p:1
i/p: 123456789
o/p:3
i/p: ab
o/p:6
i/p: A1234B
o/p:2
i/p: A1234a@4
o/p:-1
i/p: 1234567
o/p:3
i/p: a123456
o/p: 2
i/p:abcdef127
o/p:2
'''
S = input()
upper = False
lower = False
digit = False
special = False
for i in S:
    if i.isupper():
        upper = True
    elif i.islower():
        lower = True
    elif i.isdigit():
        digit = True
    elif not i.isalnum():
        special = True
#m=4-(u+l+d+s)
#if (len(S)+m)<8 print(8-len(S)
#else print(m)
if lower and digit and special:
    result = -1
elif lower and digit:
    result = 2
elif upper and digit:
    result = 2
elif digit and not (upper or lower or special):
    result = 3
elif special and not (upper or lower or digit):
    result = 1
elif lower and digit and not (upper or special):
    result = 2
elif lower:
    result = 6
else:
    result = 0
print(result)


        
