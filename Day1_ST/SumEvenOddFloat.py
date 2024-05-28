'''input="5 6 2 1 0.5 2.2"
output=oddsum -6
       evensum -8
       floatsum -2.7
Num=list(map(int,input().split()))
OS,ES,FS=0,0,0
for i in Num:
    if(i%2==0):
        ES=ES+int(i)
    else:
        OS=OS+int(i)
    if '.' in Num:
        FS=FS+float(i)
print("even numbers sum -",ES)
print("odd numbers sum -",OS)
print("float numbers sum -",FS)
'''
Num = input().split()
OS, ES, FS = 0, 0, 0
for num in Num:
    if '.' in num:  
        FS += float(num)
    else:
        i = int(num)
        if i % 2 == 0:
            ES += i
        else:
            OS += i
print("even numbers sum -", ES)
print("odd numbers sum -", OS)
print("float numbers sum -", FS)
