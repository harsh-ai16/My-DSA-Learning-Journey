#Method 1 Using set
nums=list(map(int,input("The Numbers in the list").split()))
s=set(nums)
d={}
for i in s:
    d[i]=nums.count(i)

print(d)
#Time Complexity Will Be O(N²) or O(N+KN) : K no of unique elements

#Method 2 using iteration 
a={}
for i in range(len(s)):
    if nums[i] in a:
        a[nums[i]]+=1
    else:
        a[nums[i]]=1
print(a)
#Time complexity O(N) ,space Complexity O(N)

#Method 3 using get function
b={}
for i in range(len(nums)):
    b[nums[i]]=b.get(nums[i],0)+1
print(b)
#Time Complexity will be O(N)