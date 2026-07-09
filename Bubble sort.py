""" Bubble Sort """

#Ascending Order
num=[1,3,9,0,6,5,4,8,7]
n=len(num)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)


#Descending Order
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if num[j]<num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)

#Time Complexity is O(N²){For average and Worst Case} and Space complexity is O(1)

''' Best Time complexity for best case for which array should be already Sorted will be O(N)'''
num1=[1,2,3,4,5,6,7,8,9]
def bubblesortbestcase(num1):
    n=len(num1)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if num1[j]>num1[j+1]:
                num1[j],num1[j+1]=num1[j+1],num1[j]
                is_swap=True
        if is_swap==True:
            return num1
    
x=bubblesortbestcase(num1)
print(x)
