price=list(map(int,input().split()))
p=0
b=price[0]
for i in range(len(price)-1):
    if i>i+1:
        b=price[i+1]
        p=b-p[i]
else:
    print(0)    
print(p)
               
#p=p+(price[i]-price[i-1])
 #   elif price[0]==max(price) or price[-1]==min(price):
  #      print(0)
