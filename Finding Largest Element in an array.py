num=[1,3,-90,6,5,89,43,90]

n=num[0]# or n = float("-inf")

#Using If condition
for i in num:
    if i>n:
        n=i
    else:
        pass
print(n)


#Using Max function 
for i in num:
    n=max(n,i)
print(n)