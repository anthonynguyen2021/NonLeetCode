# Time = O(n) - find the length of the list and traverse it again to get to the new tail. At most 2n.
# Space = O(1) - Using constant number of pointers

# Idea of solution: If we had the pointer to the head, tail, new tail, we can get the shifted linked list. The new head is just newTail.next. The oldTail connects to the old head.
# To get to the tail, you need to traverse the list. It's a good idea to keep track of the length of the list since k is an integer. We may need to make sure that
# k is in the interval (-l, l) where l is the length of the list. Using this, we need to figure out how many steps from the head we need to take to get to the new tail. 
# We note that if k < 0, then we take -k-1 steps. If k > 0, we take l-k-1 steps. Try this on our test case to see. 
# See line 17-23 to see this idea in action. 
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
