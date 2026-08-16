""" Introduction to Binary Search """
# Binary search can only be implemented in a Sorted Array

nums=[3, 7, 12, 18, 24, 31, 39, 45, 52, 61, 73, 86, 94, 107, 119]
Target = 52
n=len(nums)

def binarysearch():
    high=n-1
    low=0
    while low<=high:
        mid=(high+low)//2
        if nums[mid]==Target:
            return mid
        elif nums[mid]>Target:
            high=mid-1
        else:
            low=mid+1
    return -1

print(binarysearch())

# Time complexity is O(log₂(N))

