nums=[10,20,30,5,10,50]
s1=0
m=max(nums)
for i in range(len(nums)):
    if i==0 or nums[i] > nums[i-1]:
        s1=s1+nums[i]
    else:
        s1=nums[i]
    if s1>m:
        m=s1
print(m)
    
    
