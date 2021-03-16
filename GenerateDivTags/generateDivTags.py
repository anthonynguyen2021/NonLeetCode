# Time = O((2n)! / n!^2 * (n+1)) | Space = T(n) * 11n
def generateDivTags(numberOfTags):
    listMatchedTags = []
	buildValidMatchedTags(numberOfTags, numberOfTags, "", listMatchedTags)
    return listMatchedTags

def buildValidMatchedTags(left, right, currentString, result):
	if left > 0:
		buildValidMatchedTags(left-1, right, currentString + "<div>", result)
	
	if left < right:
		buildValidMatchedTags(left, right-1, currentString + "</div>", result)
		
	if right == 0:
		result.append(currentString)
