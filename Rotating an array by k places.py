"""Roatating an array by K places """

#Using Python Slicing
nums = [3, 1, 5, 2, 3, 7, 5, 8, 1, 9]
k=int(input("the places to be shift"))
n=len(nums)
k%=n

nums[:]=nums[n-(k):n]+nums[0:n-k]
print(nums)
#Time complexity is O(N) and space complexity id O(1)

#Using Loop
temp=nums[n-(k):n]
for i in range(n-(k+1),-1,-1):
    nums[i+k]=nums[i]
nums[0:k]=temp
print(nums)
#Time complexity is O(N-k) and space complexity is O(k)

#Using Three Reversal Approach

def rotate(nums, k):
    n=len(nums)
    k%=n
    def func(l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

    func(n-k,n-1)
    func(0,n-k-1)
    func(0,n-1)
#Time complexity is O(N) and space complexity id O(1)