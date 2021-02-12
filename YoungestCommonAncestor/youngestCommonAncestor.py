# Idea of Solution: 

# Time = O(h)
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
