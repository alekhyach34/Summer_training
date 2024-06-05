#s='xyzabcdefklmnopqefgh' o/p:7
'''s = 'xyzabcdefklmnopqefgh'
m=max(s)
#slen = 1
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        slen += 1
    else:
        m= max(m,slen)
        slen = 1
m= max(m,slen)
print(m)
'''
#s = 'abcde'
s = 'xyzabcdefklmnopqefgh'
m= 0
c= 1
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        c+=1
    else:
        if c>m:
            m=c
        c=1
if c>m:
    m=c
print(m)
