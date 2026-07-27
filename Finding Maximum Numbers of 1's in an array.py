""" Finding Maximum Numbers of 1's in an Array """

nums = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]
nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c=0
result=0
n=len(nums)
for i in range(0,n):
    if nums[i]==1:
        c+=1
        if c>result:
                result=c
        
    else:
        c=0
        
print(result)
# Time Complexity is O(N) and space complexity is O(1)