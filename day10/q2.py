'''i/p:[4,9,8,2,14,3,15,6]
o/p:4 2 8 3 5 6 9 14
explanation:
4 8 9 2 14 3 5 6
  2 8 9 14 3 5 6
    8 9 14 3 5 6
      3 9 14 5 6
        5 9 14 6
          6 9  14'''
a=list(map(int,input().split()))
for i in range(len(a)-2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)
'''
a= [4, 9, 8, 2, 14, 3, 15, 6]
def custom_sort(arr):
    n = len(arr)
    for i in range(0, len(arr)-2, 3):
        arr[i:i + 3] = sorted(arr[i:i + 3])
input_list = [4, 9, 8, 2, 14, 3, 15, 6]
custom_sort(input_list)
print(input_list)'''
