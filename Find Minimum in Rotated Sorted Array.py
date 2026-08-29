nums = [3,4,5,1,2]
target=1
n=len(nums)

def shortest():
    high=n-1
    low=0
    while low<high:
        mid=(high+low)//2

        if nums[mid]>=nums[high]:
            low=mid+1
        else:
            high=mid
    return nums[low]
    
print(shortest())