''' Optimal approach '''
nums = [9,6,4,2,3,5,7,0,1]
n=len(nums)
s=(n*(n+1))//2
c=0
for i in nums:
    c+=i

missing_number=(s-c)
print(missing_number)
# Time complexity is O(N) and Space complexity is (1)


''' Brute force approach '''
def func(nums):
    for i in range(0,n+1):
        if i not in nums:
            return i
print(func(nums))
# Time complexity is O(N²) and Space complexity is O(1)

''' Using dictionary ( Better Approach ) '''

d={}
for i in range(0,n+1):
    d[i]=0

for i in nums:
    d[i]=d.get(i,0)+1

for key,value in d.items():
    if value==0:
        print(key)
# Time complexity is O(3N) and space Complexity is O(N)