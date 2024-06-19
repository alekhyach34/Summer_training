n=[2,5,2,3,6,7,1,0,5,7]
n1=[2,5,5,5,6,7,7,7,7]
l = [0] * len(n)
r= [0]*len(n)
m=0
m1=0
s=0
for i in range(len(n)):
  if n[i]>m:
    m=n[i]
  l[i]=m
for i in range(len(n)-1,-1,-1):
  if n[i]>m1:
    m1=n[i]
  r[i]=m1
for i in range(len(n)):
  # Calculate the minimum of l[i] and r[i], then subtract n[i], and finally take the absolute value
  s=s+(abs(min(l[i],r[i]) - n[i])) 
print(s)
