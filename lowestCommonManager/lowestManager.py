# Explanation of solution: Note direct reports just mean children. You can think of the documents a a node. Note topManager is a node. The idea is at a given node with manager node 
# of the two node reportOne and node reportTwo, we need to find the youngest manager. We think of a recursive method. Given a manager node and the two document nodes, the method return
# None if the two documents are not in the subtree rooted at manager. Otherwise, it'll return a youngest manager of the two document (nodes). Also, the recursive method should return
# the number of documents seen in the root node at manger. So we use a class to cache these # of documents and youngest manager. To build the topManager solution, 
# we count the number of documents seen in the children of topManager. We add these number of documents. If we haven't seen two, we should None as youngest manager and the sum
# as total documents seen.

# Time = O(n)
# Space = O(h) where h is the height of the tree
def getLowestCommonManager(topManager, reportOne, reportTwo):
    	return getLowestManager(topManager, reportOne, reportTwo).lowestManager

def getLowestManager(manager, reportOne, reportTwo):
	numDocuments = 0
	for document in manager.directReports:
		documentManager = getLowestManager(document, reportOne, reportTwo)
		if documentManager.lowestManager:
			return documentManager
		numDocuments += documentManager.numDocuments
	if manager == reportOne or manager == reportTwo:
		numDocuments += 1
	lowestManager = manager if numDocuments == 2 else None
	return Manager(lowestManager, numDocuments)

class Manager:
	def __init__(self, lowestManager, numDocuments):
		self.lowestManager = lowestManager
		self.numDocuments = numDocuments

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
