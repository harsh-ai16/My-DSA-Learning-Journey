"""Roatating an array by K places """

#Using Python Slicing
nums = [3, 1, 5, 2, 3, 7, 5, 8, 1, 9]
k=int(input("the places to be shift"))
n=len(nums)
k%=n

nums1=nums[n-(k):n]+nums[0:n-k]
print(nums1)


#Using Loop
temp=nums[n-(k):n]
for i in range(n-(k+1),-1,-1):
    nums[i+k]=nums[i]
nums[0:k]=temp
print(nums)