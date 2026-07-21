# Removing dublicates from an array or list

#Using Dictionary 
nums = [3, 1, 5, 2, 3, 7, 5, 8, 1, 9]
n=len(nums)
d={}
for i in range(0,n):
    d[nums[i]]=0

l=0
for k in d:
    nums[l]=k
    l+=1
print(f"No. of distinct elements {l} and array is {nums}")
# time complexity is O(2N) and Space complexity id O(N)

#Using Single loop and Sorted array(**must**)
num = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8]
i=0
j=i+1
m=len(num)
if m==1:
    print(1)

while j<m:
    if num[i]!=num[j]:
        i+=1
        num[i],num[j]=num[j],num[i]
    j+=1
print(f"No. of distinct elements {i+1} and array is {num}")

# Time complexity is O(N) and space complexity is O(1)



