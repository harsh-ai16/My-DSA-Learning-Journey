""" Four Sum Problem """
nums = [4,3,2,1,0,0,-1,-2,-3,-4]
target = 0
n=len(nums)

# Brute force approach
def brute():
    mysetr=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        temp=[i,j,k,l]
                        temp.sort()
                        mysetr.add(tuple(temp))
    return [ans for ans in mysetr]
print(brute())
# Time complexity is O( N^4 ) and Space complexity is O( Number of quadruplets ) 


# Better approach
mysets=set()
for i in range(n):
    for j in range(i+1,n):
        tempset=set()
        for k in range(j+1,n):
            l=target-(nums[i]+nums[j]+nums[k])
            if l in tempset:
                temp=[nums[i],nums[j],nums[k],l]
                temp.sort()
                mysets.add(tuple(temp))
            tempset.add(nums[k])
print(list(mysets))
# Time Complexity is o(N³) and space complexity is O( N + Number of triplets )

# Optimal Approach
nums.sort()
myset=[]
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue

    for j in range(i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            total=nums[i]+nums[j]+nums[k]+nums[l]
            if total < target:
                j+=1
            elif  total > target:
                l-=1
            else:
                myset.append([nums[i],nums[j],nums[k],nums[l]])
                j+=1
                l=-1

                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while k<l and nums[l]==nums[l+1]:
                    l-=1

print(myset)
                

