"""Finding Fibonacci series using Recursions"""
n=int(input("The number"))
def num(n):
    if n==1 or n==0:
        return n
    return num(n-1)+num(n-2)

print(num(n))