'''s='abc'
t='bac'
ans=[]
for i in range(len(s)-1):
    for j in range(len(t)-1):
        ans += abs(s[i]-t[j])
print(ans)
    '''
s = 'abc'
t = 'bac'
ans = 0  

for i in range(min(len(s), len(t))):
    #ans += abs(ord(s[i]) - ord(t[i]))
     ans += abs(i - t.index(s[i]))
print(ans)
