''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
# Optimal Solution 
class Solution:
    def lengthOfLoop(self, head):
        slow=head
        fast=head
        count=1
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                while slow.next!=fast:
                    slow=slow.next
                    count+=1
                return count

        return 0
# Time Complexity is O(N) and Space Copplexity is O(1)

# Brute force Approach 
    def lengthOfLoop_brute(self, head):
        current=head
        travel=0
        dict={}
        while current is not None:
            if current in dict:
                return travel-dict[current]
            dict[current]=travel
            travel+=1
            current=current.next
        return 0
# Time Complexity is O(N) and Space Copplexity is O(N)
    

