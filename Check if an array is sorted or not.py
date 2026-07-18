# Check if an array is sorted or not

#Using bubble sort idealogy
nums=[1,2,3,4,5,6,7,8,9]
n=len(nums)
def func(nums):
    is_sorted=True
    for i in range(n-2,-1,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                is_sorted=False
                break
    return is_sorted

print(func(nums))

#Using single iteration
def check(nums):
    is_sorted=True
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            is_sorted=False
    return is_sorted

print(check(nums))