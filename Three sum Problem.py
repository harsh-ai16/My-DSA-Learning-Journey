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