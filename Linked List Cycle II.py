""" Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

# Brute Force approach
    def detect_Cycle_brute(self, head):
        present=set()
        current=head
        while current is not None:
            if current in present:
                return current
            present.add(current)
            current=current.next
        return None


    def detect_Cycle_optimal(self, head):
        slow=head
        fast=head

        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None