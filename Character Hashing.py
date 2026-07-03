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


#Method 3 Using hashing and Ascii function odr()
 
 