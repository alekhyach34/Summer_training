words = ['leet','code']
x = 'e'
ans=[]
for i in range(len(words)):
    if x in words[i]:
        ans.append(i)
print(ans)
