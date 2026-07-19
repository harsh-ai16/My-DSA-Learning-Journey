nums=[1,2,3,4,6,5,7,8,9]

#Smallest Element in an array
smallest=float("inf")
for i in nums:
    if i<smallest:
        smallest=i
print(smallest)


#Second Smallest element in an array

#using double iterations
def secondsmallest(nums):
    smallest1=float("inf")
    Second_smallest=float("inf")
    for i in nums:
        if i<smallest1:
            Second_smallest=smallest
            smallest=i
    for i in nums:
        if i<Second_smallest and i!=smallest1:
            Second_smallest=i
    return Second_smallest

#Using Single iteration

def S_smallest(nums):
    smallest1=float("inf")
    Second_smallest=float("inf")

    for i in nums:
        if i<smallest1:
            Second_smallest=smallest1
            smallest1=i
        elif i<Second_smallest and i!=smallest1:
            Second_smallest=i
    return Second_smallest
print(S_smallest(nums))