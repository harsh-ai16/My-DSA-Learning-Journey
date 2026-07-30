''' Maximum Subarray Sum '''
nums=[4, -6, 5, 2]
n=len(nums)

# Using Brute Force Approach 
c=nums[0]

for i in range(n):
    previous_sum=0
    for j in range(i,n):
        previous_sum+=nums[j]
        if previous_sum>c:
            c=previous_sum
print(c)
#Time complexity is O(N²) and Space Complexity is O(1)

# Kadane's Algorithm ( optimal solution ) 
maxs=nums[0]
current_sum=0
for i in range(0,n):
    current_sum+=nums[i]
    if current_sum<0:
        current_sum=0
    if current_sum>maxs:
        maxs=current_sum
print(maxs)
#Time complexity is O(N) and Space Complexity is O(1)