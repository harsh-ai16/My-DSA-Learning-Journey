nums = [3,4,5,1,2]
target=1
n=len(nums)

def shortest():
    high=n-1
    low=0
    mini=float("inf")
    while low<high:
        mid=(high+low)//2

        if nums[mid]<=nums[high]:
            mini=min(nums[mid],mini)
            high=mid-1
        else:
            mini=min(nums[low],mini)
            low=mid+1
    return mini
    
print(shortest())
# Time Complexity is O( Log(N) ) and Space Complexity is O(1)