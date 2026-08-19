""" Implementation of lower bound """
nums=[1, 2, 2, 2, 3, 5]
target=2
n=len(nums)
lb=n
high=n-1
low=0
while low<=high:
    mid=(high+low)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)

""" Implementation of Upper bound """
ub=n
high_=n-1
low_=0
while low_<=high_:
    mid=(high_+low_)//2
    if nums[mid]>target:
        ub=mid
        high_=mid-1
    else:
        low_=mid+1
print(ub)