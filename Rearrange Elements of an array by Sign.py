""" Rearrange Elements by their sign"""
nums = [3,1,-2,-5,2,-4]
n=len(nums)

#Better Approach
nl=[]
positive=[]
negative=[]
for i in range(0,n):
    if nums[i]>0:
        positive.append(nums[i])
    else:
        negative.append(nums[i])
for i in range(0,n//2):
    nl.append(positive[i])
    nl.append(negative[i])

print(nl)
## Time Complexity is O(N) and space complexity is O(N)

#Optimal Approach
newl=[0]*n
j=0
k=1
for i in range(0,n):
    if nums[i]>=0:
        newl[j]=nums[i]
        j+=2

    else:
        newl[k]=nums[i]
        k+=2

print(newl)
## Time Complexity is O(N) and space complexity is O(1)


    



