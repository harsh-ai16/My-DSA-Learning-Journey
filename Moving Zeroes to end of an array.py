nums=[0, 0, 1, 5, 9]
n=len(nums)
i=float("inf")

for k in range(0,n):
    if nums[k]==0:
        i=k
        break

if i<n:
    j=i+1
    while j<n:
        if nums[i]==0:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
    print(nums)
else:
    print(nums)
    
