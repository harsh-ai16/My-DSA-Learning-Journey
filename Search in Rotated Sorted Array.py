nums = [12, 15, 18, 21, 2, 5, 8, 10]
target=8
n=len(nums)
def binary():
    low=0
    high=n-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]==target:
            return mid
        
        if nums[mid]<=nums[high]:
            if nums[mid]<= target <=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<= target <=nums[mid]:
                high=mid-1
            else:
                low=mid+1
    return -1

print(binary())
# Time Complexity is O( Log(N) ) and Space Complexity is O(1)