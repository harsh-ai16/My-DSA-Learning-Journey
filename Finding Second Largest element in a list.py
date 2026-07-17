num=[1,3,-90,6,5,89,43,90]
largest=float('-inf')
smallest=float("-inf")

for i in num:
    if i>largest:
        largest=i
for i in num:
    if i>smallest and i<largest:
        smallest=i
print(smallest)
# Time complexity is O(2N)


for i in num:
    if i>largest:
        smallest=largest
        largest=i
    elif i>smallest and i!=largest:
        smallest=i
print(smallest)

#Time comlexity is O(N)