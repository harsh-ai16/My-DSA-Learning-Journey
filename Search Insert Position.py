nums = [1, 3, 5, 6, 8, 10, 13, 17]
target=5
n=len(nums)
lb=-1
high=n-1
low=0

while low<=high:
    mid= (high+low)//2

    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1

print(lb)
