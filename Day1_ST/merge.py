'''a = list(map(int , input().split()))
b= list(map(int , input().split()))
first = a[0]
second = b[0]
i = 0
j = 1
while i < len(a) :
    if a[i] < first and b[j]<second:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    i += 1
while j<len(b):
    if b[j]<second:
        tmp = b[i]
        b[i] = b[j]
        b[j] = tmp
    i += 1
c=a+b
print(c)

# Input the lists
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Function to sort a list using insertion sort with while loops
def insertion_sort(lst):
    n = len(lst)
    i = 1
    while i < n:
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        i += 1
    return lst

# Sort both lists
a = insertion_sort(a)
b = insertion_sort(b)

# Merge the two sorted lists
c = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Append remaining elements if any
while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

# Print the merged sorted list
print(c)'''
a = list(map(int , input().split()))
b= list(map(int , input().split()))
i,j=0,0
c=[]
if(a[i]<b[j]):
    c.append(a[i])
    i=i+1
else:
    c.append(b[j])
    j=j+1
if(i<len(a)):
    c.extend(a[i:])
else:
    c.extend(b[j:])
print(c)