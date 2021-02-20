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
	# Time = O(V + E)
	# Space = O(V)
    def depthFirstSearch(self, array):
        array.append(self.name)  # Assuming self is never empty
		for child in self.children:
			array = child.depthFirstSearch(array)
		return array
