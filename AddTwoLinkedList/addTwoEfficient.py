# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
		
# Idea: Given two pointers left and right, we compute the ones digit and the carry.
# Create the node with value (left.value + right.value + carry) % 10 that goes into a new node in which
# the previous node points to - it's easier to create a previous node (call it preHead) set to some value 0 for ease.
# We do a while loop as long as either left or right or carry != 0. Then return prevHead.next.

# Time = O(max(m, n)) = Space where m = length of first linked list and n is the length of second.
def sumOfLinkedLists(linkedListOne, linkedListTwo):

	prev = prevHead = LinkedList(0)  # prev, prevHead points to the same class object
	carry = 0
	left, right = linkedListOne, linkedListTwo

	# The trick to getting this while loop to work simplifies the code and set leftVal / rightVal to 0 if it is None.
	while left or right or carry != 0:

		leftVal = left.value if left else 0
		rightVal = right.value if right else 0
		addVal = leftVal + rightVal + carry

		carry = addVal // 10
		ones = addVal % 10

		prev.next = LinkedList(ones)
		prev = prev.next
		left = left.next if left else None  # Nice use of ternary operator in case we have the case when left is None in which we do nothing; otherwise, we advance left by one.
		right = right.next if right else None

	return prevHead.next
