# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time = O(n) where n is the length of the list
# Space = O(1) no auxillary space.
def findLoop(head):
    slow = head.next
	fast = head.next.next
	while slow != fast:
		slow = slow.next
		fast = fast.next.next	
	locateCycle = head
	while locateCycle != slow:
		locateCycle = locateCycle.next
		slow = slow.next
	return slow 
	
