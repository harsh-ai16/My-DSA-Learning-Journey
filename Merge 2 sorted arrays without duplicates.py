arr1 = [1, 2, 2, 4, 6]
arr2 = [2, 3, 4, 4, 7]
i=0
j=0
newlist=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]==arr2[j]:
        if len(newlist)>0 and newlist[-1]!=arr1[i]:
            newlist.append(arr1[i])
            
        elif len(newlist)==0:
            newlist.append(arr1[i])
            
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        if len(newlist) == 0 or newlist[-1] != arr1[i]:
            newlist.append(arr1[i])
        i+=1
    else:
        if len(newlist) == 0 or newlist[-1] != arr2[j]:
            newlist.append(arr2[j])
        j+=1

if i<len(arr1):
    s1=set(arr1[i:len(arr1)])
    for x in s1:
        newlist.append(x)
        

if j<len(arr2):
    s2=set(arr2[j:len(arr2)])
    for y in s2:
        newlist.append(y)

print(newlist)