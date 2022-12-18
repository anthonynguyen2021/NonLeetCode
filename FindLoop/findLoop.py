

# This is an input class. Do not edit.
class LinkedList:

    def __init__(self, value):

        self.value = value
        self.next = None


# Time = O(n) where n is the length of the list
# Space = O(1) no auxillary space.
def findLoop(head):

	# Two pointers
	slow = head.next
	fast = head.next.next

	# Find out where they meet again
	while slow != fast:
		slow = slow.next
		fast = fast.next.next	

	# when head and slow meet again is the point where cycle begins
	locateCycle = head
	while locateCycle != slow:
		locateCycle = locateCycle.next
		slow = slow.next

	return slow
