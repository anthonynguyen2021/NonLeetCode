

# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: 'ListNode') -> 'ListNode':
        """
        Remark: This takes care of the case if we just have a cycle. Do a 4-cycle case. 
        Once we enter the if statement in detectCycle, slow is at head. 

        # Time = O(n) where n = # of nodes in the linked list
        # Space = O(n)
        """
        visit = set()
        current = head

        while current:

            if current in visit:
                return current

            visit.add(current)
            current = current.next

        return None
