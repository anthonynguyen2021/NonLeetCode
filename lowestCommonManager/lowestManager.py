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
