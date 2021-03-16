# Explanation of solution: One can prove the catalin numbers C_n := (2n)! / (n! * n! * (n+1)) is equal to the number of such
# valid brackets in this problem using n symbols of '[' and ']'. For the space complexity, we have that '[' and ']' corresponds to
# '<div>' and '</div>', respectively. But they consists of 11 characters for each valid enclosure. So S(n) = T(n) * 11n = T(n) * n.

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
