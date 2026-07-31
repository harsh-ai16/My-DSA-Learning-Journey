""" Classic Two Sum Problem of Leetcode"""

nums=[2,7,11,15]
target=9
n=len(nums)

# Brute force solution
def func(nums):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

print(func(nums))
# Time Complexity is O(N²) and space complexity is O(1)

#Optimal Solution
def twosum(nums,target):
    d={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in d:
            return [d[remaining],i]
        d[nums[i]]=i

print(twosum(nums,target))
# Time Complexity is O(N) and space complexity is O(N)