# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time = O(n)
# Space = O(1)

# Explanation: Use a while loop in this problem. The idea is use a pointer that checks if 
# the current and its neighbors equal, then change current.next to move two over. The breaking condition
# is if the current pointer is empty, break out. After you check if the current and its neighbors don't
# equal, move the current <- current.next

def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
	while current:
		while current.next and current.value == current.next.value:
			current.next = current.next.next
		current = current.next
	return linkedList
