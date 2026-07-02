nums=int(input("The Number"))
list=[i for i in range(1,nums+1) if nums%i==0]
print(list)
#Time complexity O(N)
'''If we iterate upto half of Nums still it will give all factors excluding the num itself 
and Time complexity reduces to O(N/2)'''

from math import sqrt
l=[]
for i in range(1,int(sqrt(nums))+1):
    if nums%i==0:
        l.append(i)
        if nums//i!=i:
            l.append(nums//i)

print(sorted(l))

"""In this Case Time complexity is O(sqrt(N))+O(Nlog(N)) and space complexity is O(K) : k is number of factors"""