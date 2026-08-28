nums = [4, 5, 6, 0, 0, 1, 2, 2, 3]
n=len(nums)
target=7
def binary():
    low=0
    high=n-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]==target:
            return True
        if nums[high]==nums[low]==nums[mid]:
            high-=1
            low+=1
            continue
            
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
    return False

print(binary())