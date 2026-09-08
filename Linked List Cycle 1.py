""" Linked List Cycle """
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

 # Brute force approach
class Solution(object):
    def hasCycle(self, head):
        present=set()
        current=head
        while current is not None:
            if current in present:
                return True
            present.add(current)
            current=current.next

        return False
# Time complexity is O(N) and Space compexity is O(N)

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False
# Time complexity is O(N) and Space compexity is O(1)