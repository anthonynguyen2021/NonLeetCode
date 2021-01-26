# Time = O(n) - find the length of the list and traverse it again to get to the new tail. At most 2n.
# Space = O(1) - Using constant number of pointers

# Idea of solution: 
def shiftLinkedList(head, k):
    # Find length of linkedlist
	length = 1
	oldTail = head
	while oldTail.next:
		length += 1
		oldTail = oldTail.next
	
	offset = abs(k) % length
	if offset == 0:
		return head
	numSteps = length - offset if k > 0 else offset
	newTail = head
	for i in range(1, numSteps):
		newTail = newTail.next
	
	newHead = newTail.next
	oldTail.next = head
	newTail.next = None
	return newHead 


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
