""" Insertion Sort """

class Solution:
#Ascending Order
    def insert_Sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr

arr=[1,2,4,3,7,5,8,0,9]
obj=Solution()
print(obj.insert_Sort(arr))

class Solutions:
#Descending Order
    def insert_Sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]<key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr

arr=[1,2,4,3,7,5,8,0,9]
obj1=Solutions()
print(obj1.insert_Sort(arr))

#Time Complexity is O(N²) and Space Complexity is O(1)