nums = [10, 30, 20, 2, 3, 4, 1, 5]
n=len(nums)
c=0

# Optimal Approach
e=set(nums)
if n==0:
    print(0)
else:
    for i in range(0,n):
        l=0
        d=nums[i]
        if d-1 not in e:
            while d+1 in e:
                l+=1
                d+=1
            c=max(c,l)
    print(c+1)
#Time Complexity is O(N) and Space complexity is O(1)

# Better Approach (Using Sorting)
nums1 = [10, 30, 20, 2,2, 3, 4, 1,1, 5]
nums1.sort()
count=0
last_smaller=float('-inf')
longest=0
for i in range(0,n):
    num=nums1[i]
    if num==last_smaller:
        continue
    elif num-1==last_smaller:
        count+=1
        last_smaller=num
    elif num-1!=last_smaller:
        count=1
        last_smaller=num
    longest=max(count,longest)
print(longest)
#Time Complexity is O(Nlog(N)) and Space complexity is O(1)