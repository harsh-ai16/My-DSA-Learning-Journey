s="azyxyyzaaaa" #contraints : All Letters are in smaller case
q=["d","a","y","x"]

#Method 1 using 
for i in q:
    c=0
    for j in s:
        if i==j:
            c+=1
    print(i,c)

#Method 2 using frequnecy dictionary
d={}
for i in s:
    d[i]=d.get(i,0)+1

for j in q:
    if j in d:
        print(j,d[j])
    else:
        print(j,"0")
#Time Complexity is O(M+n) and Space complexity is O(n)

#Method 3 Using hashing and Ascii function odr()
hash_list=[0]*26
for i in s:
    ascii_value=ord(i)
    index=ascii_value-97
    hash_list[index]+=1

for i in q:
    ascii_value=ord(i)
    print(i,hash_list[ascii_value-97])
#Time Complexity is O(M+n) and space complexity O(1)