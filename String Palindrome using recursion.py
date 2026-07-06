n=input("String : ")
s=list(n)
def pali(n,l,r):
    if l>=r:
        return n
    n[l],n[r]=n[r],n[l]
    return pali(n,l+1,r-1)

print(pali(s,0,len(n)-1)==list(n))
