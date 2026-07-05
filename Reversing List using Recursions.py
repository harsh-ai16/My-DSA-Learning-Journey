nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse(nums,left,right):
    if left>=right:
        return nums
    nums[left],nums[right]=nums[right],nums[left]
    return reverse(nums,left+1,right-1)

x=(reverse(nums,0,9))
print(x)
 