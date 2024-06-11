def longes_substr(s):
    start=0
    max_len=0
    d={}
    for i in range(len(s)):
        if s[i] in d and d[s[i]]>=start:
            start=d[s[i]]+1
        d[s[i]]=i
        max_len=max(max_len,i-start+1)
    return max_len
s="abcdeefghijkl"
print(longes_substr(s))
