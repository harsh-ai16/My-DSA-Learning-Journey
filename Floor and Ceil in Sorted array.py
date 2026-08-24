nums = [2, 5, 8, 12, 15, 19, 23, 27, 31, 36]
n=len(nums)

target=2
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
