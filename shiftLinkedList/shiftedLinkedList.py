# Time = O(n) - find the length of the list and traverse it again to get to the new tail. At most 2n.
# Space = O(1) - Using constant number of pointers

# Idea of solution: If we had the pointer to the head, tail, new tail, we can get the shifted linked list. The new head is just newTail.next. The oldTail connects to the old head.
# To get to the tail, you need to traverse the list. It's a good idea to keep track of the length of the list since k is an integer. We may need to make sure that
# k is in the interval (-l, l) where l is the length of the list. Using this, we need to figure out how many steps from the head we need to take to get to the new tail. 
# We note that if k < 0, then we take -k-1 steps. If k > 0, we take l-k-1 steps. Try this on our test case to see. 
# See line 22-33 to see this idea in action. Line 27-28 can be viewed as moving the current node -k-1 times if k < 0. Otherwise, move n+1 -k-1 to get to the newTail where l = n+1.

# General idea how to pick the number of steps:
# 0 -> 1 -> .... -> n -> Null
# If k > 0, we can think of the null node is the n+1 position. So we have (n+1) - k = n+ 1 - k position to get to the new head (we're using 0-based positioning). n+1 -k-1 for the new head.
# If k < 0, we can march |k| to get to the new head. -k-1 to get to the new tail. 
def shiftLinkedList(head, k):
    	# Find length of linkedlist
	length = 1
	oldTail = head
	while oldTail.next:
		length += 1
		oldTail = oldTail.next
	
	# Distance to travel from the head (left or right of the head - can think of left of the head as the tail). 
	offset = abs(k) % length
	if offset == 0:
		return head
	# Given 0 -> 1 -> .... -> n where length is n+1
	# How many steps from the head, I can get to the new head
	numSteps = length - offset if k > 0 else offset
	
	# Advance the newTail pointer numSteps-1 times to get to the newTail
	newTail = head
	for i in range(1, numSteps):
		newTail = newTail.next
	
	# Get the newHead, connect the oldTail to the oldHead. The newTail points to None.
	newHead = newTail.next
	oldTail.next = head
	newTail.next = None
	
	return newHead 


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
