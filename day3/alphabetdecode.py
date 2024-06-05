#i/p: d, key 5 o/pb: y || i/p: khoor, key=3 o/p:hello input will be always in lowe rcase
'''s=input()
key=int(input())
result=""
for i in s:
    if i.isalpha():
        shift=ord(i)-key
        if i.islower():
            if shift<ord('a'):
                shift=shift+26
                result=result+chr(shift)
            else:
                result=result+chr(shift)
print(result)
'''
a='bvec'
b=4
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)
