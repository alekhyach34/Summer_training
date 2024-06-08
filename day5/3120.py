word = "aaAbcBC"
c=0
a=set(word)
for i in a:
    if (i.islower() and i.upper() in a):
        c+=1
print(c)
        