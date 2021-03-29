# This is the class of the input root. Do not edit it.
class BinaryTree:
    	def __init__(self, value, left=None, right=None):
        	self.value = value
        	self.left = left
        	self.right = right
# Explanation: The right sibling tree is connect every node to its right node in the complete binary tree version. This means that if a node to the right of it in the same depth
# is Null, that node points to null. The idea of this method is to write a recursive method that does the following: At a tree rooted at node, we call the function at
# the tree rooted at node.left and this function connects all of its nodes to its right sibling where we consider all tree, so that we can connect all the nodes in the tree rooted
# at node.left to its right sibling. Assume that is done, we connect node to its right sibling. Next, we call the recursive method on node.right where we do the same as we connect all
# the nodes in the subtree rooted at node.right to its right sibling. Node that at node, to connect to its right sibling, we need to know if its parent is Null or not. If it is,
# we set node.right = None. If not, we know that node's parent points to its right sibling (one of the pointers). If the node is a left sibling, we change the right pointer
# to point to its parent's right child. If the node is a right sibling, we know at this point that its parent right pointer points to its right sibling. At this point,
# we check if node's parent's right sibling is None or not. If None, node.right = None. Otherwise, node.right = parent.right.left. Remark: Note that before we 
# make the call to the recusrive method on node.right and before we mutated node.right, we save that to a variable right = node.right and later, call on the recursive method
# on that right node - right.
		
# Complexities explanation: The space comes from the call on the function call stack. The time comes from at each node, we do constant amount of work - connect node to its right sibling.
# Time = O(n) | Space = O(h) where h is the height of the tree
def rightSiblingTree(root):
    	mutate(root, None, False)
	return root

def mutate(node, parent, isLeft):
	if not node:
		return None
	mutate(node.left, node, True)
	right = node.right
	if not parent:
		node.right = None
	elif isLeft:
		node.right = parent.right
	else:
		if not parent.right:
			node.right = None
		else:
			node.right = parent.right.left
	mutate(right, node, False)
