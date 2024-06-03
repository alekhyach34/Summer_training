nums=[1,2,3,1,1,3]
count_goodpairs=0
'''good_pairs=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            count_goodpairs+=1
            good_pairs.append((i,j))
print(count_goodpairs, good_pairs)'''

num_counts = {}
for num in nums:
    if num in num_counts:
        count_goodpairs += num_counts[num]
        num_counts[num] += 1
    else:
        num_counts[num] = 1
print(count_goodpairs)

     
                   
