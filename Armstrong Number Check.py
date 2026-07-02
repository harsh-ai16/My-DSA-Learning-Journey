nums=int(input("The Number"))
originalnum=nums
count=0
while nums>0:
    count+=1
    nums=nums//10

sum=0
for i in str(originalnum):
    sum+=int(i)**(count)

if sum==originalnum:
    print("Yes number is Armstrong")
else:
    print("It is not")





a=len(str(nums))
total=0
while nums>0:
    b=nums%10
    total+=b**a
    nums=nums//10

if total==originalnum:
    print("Number is armstrong")
else:
    print("not")