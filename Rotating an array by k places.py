"""Roatating an array by K places """

#Using Python Slicing
nums = [3, 1, 5, 2, 3, 7, 5, 8, 1, 9]
k=int(input("the places to be shift"))
n=len(nums)
nums1=nums[n-1:n-(k+1):-1]+nums[0:n-k]
print(nums1)


#Using Loop
for i in range()