# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
# Time = O(v + e)
# Space = O(e) 
    def breadthFirstSearch(self, array):
        queue = []
	queue.append(self)
	while queue:
		currentNode = queue.pop(0)
		array.append(currentNode.name)
		for neighbor in currentNode.children:
			queue.append(neighbor)
	return array 
