'''input range:300 400
output: numbers divisible by 7 between 300 and 400 include the range numbers
c=0
for i in range(300,400):
    if (i%7==0):
        c+=1
print(c) (300/7) - (400/7)'''
c=0
for i in range(300,400):
    if (i%7==0):
        c+=1
print(c)
