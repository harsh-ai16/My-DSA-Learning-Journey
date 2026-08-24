nums = [2, 5, 8, 12, 15, 19, 23, 27, 31, 36]
n=len(nums)

target=6
floor=-1
ceil=-1

# Optimal Approach 
high=n-1
low=0
while low<=high:
    mid=(high+low)//2

    if nums[mid]==target:
        floor=mid
        ceil=mid
        break
    elif nums[mid]>target:
        ceil=mid
        high=mid-1
    else:
        floor=mid
        low=mid+1

print(nums[floor],nums[ceil])
# Time complexity is  O(log₂(N)) and Space complexity is O(1)

# Brute force approach
floor1,ceil1=-1,-1
for i in range(n):
    if nums[i]==target:
        floor1,ceil1=i,i
        break
    elif nums[i]<target:
        floor1=i
    else:
        ceil1=i
        break
print(nums[floor1],nums[ceil1])
# Time complexity is O(N) and space complexity is O(1)