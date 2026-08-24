nums = [1, 2, 2, 2, 4, 5, 5, 5, 5, 7, 9, 9, 12, 15, 15, 18]
target=5
n=len(nums)

# Brute force approach 
first=-1
last=-1

for i in range(n):

    if nums[i]==target:
        if first==-1:
            first=i
        else:
            last=i

    if nums[i]>target:
        break
            
print(first,last)
# Time complexity is O(N) and space Complexity is O(1)

# Optimal Approach
def lowerbound():
    lb=-1
    low=0
    high=n-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb

def upperbound():
    ub=n
    low=0
    high=n-1
    while low<=high:
        mid=(high+low)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub

lb=lowerbound()
ub=upperbound()
print(lb,ub-1)
# Time compplexity is O(log₂(N) ) and Space Complexity is O(1)