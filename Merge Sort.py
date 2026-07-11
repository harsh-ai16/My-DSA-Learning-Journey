class Solution:
    def merge_arr(self,left,right):
        n,m=len(left),len(right)
        i,j=0,0
        r=[]
        while i<n and j<m:
            if left[i]<right[j]:
                r.append(left[i])
                i+=1
            else:
                r.append(right[j])
                j+=1
        while i<n:
            r.append(left[i])
            i+=1
        while j<m:
            r.append(right[j])
            j+=1
        return r
    
    def mergeSort(self,arr):
        s=len(arr)
        if s==1:
            return arr
        mid=s//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        l=self.mergeSort(left_arr)
        r=self.mergeSort(right_arr)
        return self.merge_arr(l,r)

arr=[3,2,6,5,4,8,0,1,7]
obj=Solution()
print(obj.mergeSort(arr))