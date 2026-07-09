""" Selection Sort """
n=[5,4,6,7,8,1,2,0,3,9]


#Ascending Order 
def sort(n):
    for i in range (0,len(n)):
        mid_index=i
        for j in range(i+1,len(n)):
            if n[j]<n[mid_index]:
                mid_index=j
        n[i],n[mid_index]=n[mid_index],n[i]
sort(n)
print(n)