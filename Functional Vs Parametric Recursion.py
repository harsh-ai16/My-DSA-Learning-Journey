'''Printing sum of N natural Numbers'''
#Parametric Recursion 
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)

func(0,1,10) #Time complexity in parametric recursion is O(N+1)
             #Space Complexity in  parametric recursion is O(N+1) (Stack Space)

#Using Functional recursion
def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
print(fun(10)) #Time Complexity in Functional recursion is O(N)
               #Space Complexity in  Functional recursion is O(N) (Stack Space)


"""Printing Factorial of N natural numbers"""

# Using Parametric Recursion
def fact(factorial,i,n):
    if i>n:
        print(factorial)
        return
    fact(factorial*i,i+1,n)
fact(1,1,5)


# Using Functional Recursion
def facto(n):
    if n==1:
        return 1
    return n*facto(n-1)
print(facto(5))