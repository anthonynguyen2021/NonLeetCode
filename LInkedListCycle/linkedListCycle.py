# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        '''
        Idea of solution:

        Use a two pointer approach: A slow and fast pointer; slow pointer jumps by 1 and fast jumps by two. If the fast pointer because empty, return False. 
        Otherwise, the fast will catch up with the slow. Draw a picture to see that at each step, the fast is 1 distance closer to the slow pointer.

        Time: O(n) where n = size of the linked list
        Space: O(n)
        '''
        visit = set()
        current = head

        while current:

            if current in visit:
                return True

            visit.add(current)
            current = current.next

        return False
