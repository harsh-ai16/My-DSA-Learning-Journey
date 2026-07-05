#Printing Numbers from 1 to n using recursions
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)

fun(5)
#It is an example of tail recursion

#Using Head Recursion
def func(i,m):
   if i>m:
    return
   print(i)
   func(i+1,m)
func(1,5)
