nums=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

#Method 1 using Nested loops
for i in m:
    c=0
    for j in nums:
        if i==j:
            c+=1
        else:
            pass
    print(i,c)
#Time Comlexity for this Method is O(N*M)



#Method 2 using Frequency dictionary
dict={}
for i in nums:
    dict[i]=dict.get(i,0)+1

for j in m:
    if j in dict:#if j<1 or j>10: print("0") if nums contains element from 1 to 10 only
        print(j,dict[j])
    else:
        print(j,"0")
#Time Complexity is O(M+N) space Complexity is O(N)

#Using Hashing Method (Only if Contraints are followed strictly)
hashlist=[0]*11

for i in nums:
    hashlist[i]+=1

for j in m:
    if j<1 or j>10:
        print(j,"0")
    else:
        print(j,hashlist[j])
#Time Complexity is O(M+N) and Space complexity is O(1)