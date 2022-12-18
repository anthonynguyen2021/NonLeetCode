# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time = O(n) where n is the largest size of both linked list
    # Space = O(n) since in the worst case, we may have n function calls in the call stack

    # Idea: Use a helper method that keeps track of the carry. Note the carry is at most 1 since a number in S = {1, ..., 9} plus another number in S yields a number at most 18, 
    # so a carry of at most 1. We implement a recursive method. So at each pair of nodes from the linked list and a carry, we add the values and add the ones digit in a new node
    # and keep track of the carry. Call the function again on the next ndoes of l1 and l2. 
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
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
