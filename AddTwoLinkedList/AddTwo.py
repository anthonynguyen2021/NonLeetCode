# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time = O(n) where n is the largest size of both linked list
    # Space = O(n) since in the worst case, we may have n function calls in the call stack
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helperAddTwoNumbers(l1, l2, 0)
    
    def helperAddTwoNumbers(self, l1, l2, carry):
        if l1 and l2:
            head = ListNode((l1.val + l2.val + carry) % 10)
            carry = 1 if l1.val + l2.val + carry > 9 else 0
            head.next = self.helperAddTwoNumbers(l1.next, l2.next, carry)
        elif l1:
            head = ListNode((l1.val + carry) % 10)
            carry = 1 if l1.val + carry > 9 else 0
            head.next = self.helperAddTwoNumbers(l1.next, l2, carry)
        elif l2:
            head = ListNode((l2.val + carry) % 10)
            carry = 1 if l2.val + carry > 9 else 0
            head.next = self.helperAddTwoNumbers(l1, l2.next, carry)
        else:
            if carry > 0:
                head = ListNode(carry)
            else:
                head = None
        return head 
