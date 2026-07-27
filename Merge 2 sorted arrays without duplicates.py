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

while i<len(arr1):
    if arr1[i]!=newlist[-1]:
        newlist.append(arr1[i])
    i+=1
        
        

if j<len(arr2):
    if arr2[j]!=newlist[-1]:
            newlist.append(arr2[j])
    j+=1

print(newlist)