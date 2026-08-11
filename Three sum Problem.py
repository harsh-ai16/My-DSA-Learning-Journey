""" Three Sum Problem """
nums = [-1,0,1,2,-1,-4]
n=len(nums)

# Brute force approach ( Three pointer method )
def _3sumbrute():
    result=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    result.add(tuple(temp))
    return [list(ans) for ans in result]
print(_3sumbrute())
# Time Complexity is O(N³) and Space xomplexity is O( Number of triplets)

# Better approach (using two pointers )

def _3sumbetter():
    resultant=set()
    for i in range(n):
        myset=set()
        for j in range(i+1,n):
            k=-(nums[i]+nums[j])
            if k in myset:
                temp=[nums[i],nums[j],k]
                temp.sort()
                resultant.add(tuple(temp))
            myset.add(nums[j])
    return [list(ans) for ans in resultant]
print(_3sumbetter())
# Time complexity is O(N²) and space complexity is O(N + Number of triplets)