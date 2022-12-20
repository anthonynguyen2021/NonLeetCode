

# This is an input class. Do not edit.
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

# Write a function that takes in the head of a singly linked list and an integer k and removes the kth
# node from the end of the list. The removal should be done in place.
# The head should remain the head. If we need to remove the head, just mutate its value and change its 
# next link. 
# Your function doesn't need to return anything. Returning the head is ok.

def removeKthNodeFromEnd(head, k):
	'''
	# Time: O(n) where n = # of nodes in the linked list
	# Space: O(1)
    # assume k in {1, ... , n}
	# linked list has length >= 2 and has at least k nodes
	'''
	left = right = head 
	count = 0

	while count != k:
		right = right.next
		count += 1

	if not right:  # modifies the head node
		head.value = head.next.value 
		head.next = head.next.next
		return head

	while right.next:
		left = left.next 
		right = right.next

	left.next = left.next.next

	return head
