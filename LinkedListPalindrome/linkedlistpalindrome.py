# Solution idea: Locate the second half of the linked list using a slow and fast pointer. Start the slow and fast pointer at the head. As long as the fast and fast.next is not None
# move fast two nodes over and move slow pointer one node over. When fast is None or fast.next is None, slow will be at the middle. 
# Reverse the second half. The two resulting linked lists can be compared value by value.
# If the linked list had odd number of items, the second has 1 more extra node except when the linked list is just 1 node. 

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time = O(n)
# space = O(1)
def linkedListPalindrome(head):
    slow = head
	fast = head 
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
	second = reverseLinkedList(slow)
	first = head 
	while first and second:
		if first.value != second.value:
			return False
		first = first.next
		second = second.next
	return True 
	
	
# Time = O(n)
# Space = O(1)
def reverseLinkedList(head):
	prev = None
	current = head
	while current:
		new = current.next 
		current.next = prev
		prev = current
		current = new
	return prev 
