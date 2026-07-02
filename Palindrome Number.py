nums=int(input("The Number"))
originalnum=nums
reverse=0
while nums>0:
    a=nums%10
    reverse=(reverse*10)+a
    nums=nums//10
if originalnum==reverse:
    print("True, it is Palindrome Number")
else:
    print("It is not Palindrome Number")

#Time Complexity is O(log₁₀(N))