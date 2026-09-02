""" Finding Middle Node of a Singly Linked List """

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optimal Approach ( Tortoise-Hare Approach )
class Solution(object):
    def middleNode(self, head):

        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
# Time complexity is O(N/2) and Space Complexity is O(1) 

# Brute Force approach
class Solution(object):
    def middleNode(self, head):
        temp=head
        total=0
        while temp is not None:
            count+=1
            temp=temp.next

        for i in range(0,total//2):
            temp=temp.next

        return temp
# Time complexity is O(3N/2) and Space Complexity is O(1) 