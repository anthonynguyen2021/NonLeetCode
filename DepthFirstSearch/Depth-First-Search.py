# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# Idea of Solution: 

	# Time = O(V + E) - For each node you visit, you have to call the function on its children (which is the number of edges)
	# Space = O(V) - return the array of all nodes visited in the dfs recursive visit approach.
    def depthFirstSearch(self, array):
        array.append(self.name)  # Assuming self is never empty
	for child in self.children:
		array = child.depthFirstSearch(array)
	return array
