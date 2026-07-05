'''Printing sum of N natural Numbers'''
#Parametric Recursion 
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)

func(0,1,10)

#Using Functional recursion
def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
print(fun(10))


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