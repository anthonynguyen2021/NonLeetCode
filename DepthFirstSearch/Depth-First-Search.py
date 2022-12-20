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

	def depthFirstSearch(self, array):
		'''
		Time = O(V + E) - For each node you visit, you have to call the function on its children (which is the number of edges).
		V = # of vertices in graph, E = # of edges in graph
		Space = O(V) - return the array of all nodes visited in the dfs recursive visit approach.

		Idea of Solution:

		We use a recursive approach. Push the current name in the array. Then call the function recursively
		on its children. In the method below, to understand what this dfs outputs, let suppose we're at a given tree node.
		Assume we have the current visited array, we visit everything including the current tree node using dfs; by visiting,
		we're adding to the array. We return that array.
		'''
		array.append(self.name)  # Assuming self is never empty

		for child in self.children:
			array = child.depthFirstSearch(array)

		return array
