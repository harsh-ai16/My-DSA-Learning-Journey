"""Using swapping and recursion"""

n=input("String : ")
s=list(n)
def pali(n,l,r):
    if l>=r:
        return n
    n[l],n[r]=n[r],n[l]
    return pali(n,l+1,r-1)

print(pali(s,0,len(n)-1)==list(n))


''' Using Index checking '''

#using Loop
left=0
right=len(n)-1

while left<right:
    if n[left]!=n[right]:
        print(False)
        break
    left+=1
    right-=1
else:
    print(True)
    
#Using Recursion

def func(n,left,right):
    if left>=right:
        return True
    if n[left]!=n[right]:
        return False
    return func(n,left+1,right-1)
print(func(n,left,right))