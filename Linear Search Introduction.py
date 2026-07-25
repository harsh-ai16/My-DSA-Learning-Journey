#this is the introduction to linear search approach and algorithm



def search(arr, x):
        for i in range(0,len(arr)):
            if arr[i]==x:
                return i
        return -1