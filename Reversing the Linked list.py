""" Reversing the Singly Linked List """


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        previous=None
        current=head
        while current is not None:
            front=current.next
            current.next=previous
            previous=current
            current=front
        return previous

# Time Complexity is O(N) and Space Complexity is O(1)