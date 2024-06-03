s='MMFFMFMFF'
c1,c2=0,0 #c=0
for i in s:
    if i=='M':
        c1+=1 #c+=1
    else:
        c2+=1  #c-=1
if c1==c2:      #c=0
    print('0')
elif(c1>c2):      #c>0
    print('M')
else:             #c<0
    print('F')
