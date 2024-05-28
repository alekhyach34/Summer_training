#s='aaabbaaaaddd'
def SWstring(s):
    c=1
    a=[]
#output a3b2a4d3
    n=len(s)
    if not s:
        return ""
    for i in range(1,n):
        if(s[i]==s[i-1]):
            c+=1
        else:
            a.append(s[i-1]+str(c))
            c=1
    a.append(s[-1]+str(c))
    return ''.join(a)
s= input()
output = SWstring(s)
print(output)
