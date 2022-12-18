# This is an input class. Do not edit.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time = O(max(m,n)) = Space = O(max(m, n)) where m is the length of the first linked list, n is the second

# We perform a while loop on the case that the left and right current pointers are not None, then we compute the ones and carries.
# Once this while loop breaks, we perform a while loop on left or right (exactly one will hold). After this breaks, the carry maybe 1 still.

def sumOfLinkedLists(linkedListOne, linkedListTwo):
	# Write your code here.

	prev = preHead = LinkedList(-1)  # prev, preHead referred to the same class object not two object with value -1
	left = linkedListOne
	right = linkedListTwo
	carry = 0

	while left and right:
		ones = (left.value + right.value + carry) % 10
		carry = (left.value + right.value + carry) // 10
		prev.next = LinkedList(ones)
		prev, left, right = prev.next, left.next, right.next

	while left or right:
		ones = (left.value + carry) % 10 if left else (right.value + carry) % 10
		if left:
			carry = (left.value + carry) // 10
		else:
			carry = (right.value + carry) // 10
		prev.next = LinkedList(ones)
		prev = prev.next
		if left:
			left = left.next
		else:
			right = right.next

	if carry != 0:
		prev.next = LinkedList(carry)
		return preHead.next
