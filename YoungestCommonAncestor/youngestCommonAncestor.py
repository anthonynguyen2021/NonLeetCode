# Idea of Solution: Find the distance from descendant1 & descendant 2 to the top ancestor. For argument sake, let's assume descandant1 is at a larger depth than descendant 2. 
# Keep traversing the ancestor of descendant 1 until both nodes are equi-distance from the top ancestor. As long as these two nodes aren't equal, look at both of their ancestors
# and repeat. 


# Time = O(h) h is the height of the tree
# Space = O(1)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):

	distanceOne = getDistanceToAncestor(topAncestor, descendantOne)
	distanceTwo = getDistanceToAncestor(topAncestor, descendantTwo)

	while distanceOne > distanceTwo:
		distanceOne -= 1
		descendantOne = descendantOne.ancestor

	while distanceOne < distanceTwo:
		distanceTwo -= 1
		descendantTwo = descendantTwo.ancestor

	while descendantOne != descendantTwo:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor

	return descendantOne


def getDistanceToAncestor(topAncestor, descendant):
	distance = 0
	while descendant != topAncestor:
		distance += 1
		descendant = descendant.ancestor
	return distance
