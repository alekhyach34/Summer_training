'''
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22]
#Method1
a=[10,4,8,3]
for i in range(len(a)):
    b.append(abs(sum(a[:i])-sum(a[i+1:])))
print(b)   #TC is O(n*n+n)
method2
def left_right_difference(nums):
    n = len(nums)
    for i in range(1, n):
        leftSum[i] = leftSum[i-1] + nums[i-1]
    for i in range(n-2, -1, -1):
        rightSum[i] = rightSum[i+1] + nums[i+1]
    for i in range(n):
        answer = [(leftSum[i] - rightSum[i])]
    return answer
nums = [10, 4, 8, 3]
output = left_right_difference(nums)
print(output)
#space complexity
nums=[10,4,8,3]
s=sum(nums)
b=[]
x=0
for i in nums:
    b.append(abs((x)-(s-i-x)))
    x=x+i
print(b)'''
nums=[10,4,8,3]
s=sum(nums)
j=0
x=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j+=1
print(nums)
