nums=int(input("The Number"))
list=[i for i in range(1,nums+1) if nums%i==0]
print(list)
#Time complexity O(N)

'''If we iterate upto half of Nums still it will give all factors excluding the num itself 
and Time complexity reduces to O(N/2)'''
