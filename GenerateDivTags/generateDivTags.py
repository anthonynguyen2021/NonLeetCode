# Explanation of solution: One can prove the catalin numbers C_n := (2n)! / (n! * n! * (n+1)) is equal to the number of such
# valid brackets in this problem using n symbols of '[' and ']'. For the space complexity, we have that '[' and ']' corresponds to
# '<div>' and '</div>', respectively. But they consists of 11 characters for each valid enclosure. So S(n) = T(n) * 11n = T(n) * n.

# Understanding the logic of this problem: Image you're at left = m and right = n.
#                       (m, n)
#                      /      \
#                   (m-1, n)   (m, n-1)
# 
# We do the right branch if m < n, which means that we used more of the '<div>' symbols than '</div>'. The left branch means
# As long as m > 0, we call the function on the left branch. In the recursive function at (m, n) and call it again on (m-1, n) and
# (m, n-1) whenever possible. Note that when n = 0, these two cases do not activate.

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
		
# Explanation #2
# Algorithm keeps track of the number of left and right parenthesis. When right hits 0, we append
# assuming that the number of left <= number of right at all times for valid string.
# Idea: First if means using a left parenthesis. Second if means use a right parenthesis
# when is a valid string. Last if means that we used all left and all right parenthesis and valid.
