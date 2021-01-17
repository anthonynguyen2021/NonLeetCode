# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Time = O(n)
        # Space = O(n) recursive call until 
        if not head or not head.next:
            return head
        else:
            last = head 
            secondToLast = last.next 
            revHead = self.reverseList(head.next)
            secondToLast.next = last
            last.next = None
            return revHead
