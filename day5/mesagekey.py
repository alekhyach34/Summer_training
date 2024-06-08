key = "the quick brown fox jumps over the lazy dog"
b=''
c=''
for i in key:
    if(i not in b and i!=" "):
        b+=i
for i in message:
    if(i!=" "):
        c=c+chr(b.index(i)+97)
    else:
        c=c+" "
 return c