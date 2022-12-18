from collections import deque

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

    # Time = O(v + e) - At each node, we push in all of its neighbors (all of its edges)
    # Space = O(v) - output is the number of vertices
    def breadthFirstSearch(self, array):
        '''
        arguments:
            self: class instance
                contains the tree structure
            array: list['name']
                contains the solution for the BFS traversal
        '''
        queue = deque([])
        queue.append(self)

        while queue:

            currentNode = queue.popleft()
            array.append(currentNode.name)

            for neighbor in currentNode.children:
                queue.append(neighbor)

        return array
