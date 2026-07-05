num=[1,2,3,4,5,6,7,8,9]
left=int(input("The starting index"))
right=int(input("The ending index"))

# while left<right:
#     num[left],num[right]=num[right],num[left]
#     left+=1
#     right-=1
while True:
    if left>=right:
        break
    num[left],num[right]=num[right],num[left]
    left+=1
    right-=1
    
print(num)