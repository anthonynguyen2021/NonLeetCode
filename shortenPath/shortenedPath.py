# Explanation: If the first character is /, we have an absolute path. Note when we split path by the character "/", we have some directory names, maybe "" due to // and ".". So
# we can filter these out using the filter funnction along with a helper method isValid to indicate True if the substring from the split method isn't "" or ".". Initialize a stack.
# We append "" if we have an absolute path. Note when we use split where the first character is "/", the first element is "". Now, we go through the filtered elements in tokens.
# If token is not "..", it's definitely not ".", "" (filtered out), we must append as these are directory names. If token is "..", we have to consider edge cases. If we have a relative
# path. So if the length(stack) == 0 at this point and token == "..", we append it; note that name1/../name2/.. are collapsed so intuitively, we don't consider these. If the stack
# has length > 0, and the top of the stack is "..", we have something that looks like ../../, so we need to append this. If the top of the stack is "", we have /.. as the beginning of 
# out path. So we do nothing. If the top of the stack is not "", we pop out since we have somethign like name1/.. which is collapsed. 

# Now, we like to join these elements in the stack by "/".join(stack). But if the length of the stack is 1, we have to consider several cases. If stack[0] == "", then just return
# "/" since everythign else with '.', "", and name1/.. are ignored or collapsed, so we have "/". If stack[0] != "", say "..", then the "/".join([".."]) returns ".." since we 
# can't join anything. Note in python, "/".join([]) yields "" since it's just the empty string in that array. Similarly, if stack[0] is a name, "/".join(stack) just yields the name
# of the relative path.

# Explanation - split is linear so O(n). filter is roughly O(n). We store roughly O(n) in tokens and stack. Join is roughly O(n). Here n is the length of path.
# Time = O(n) | Space = O(n)
def shortenPath(path):
    	absolutePath = path[0] == "/"
	tokens = filter(isValid, path.split("/"))
	stack = []
	if absolutePath:
		stack.append("")
	for token in tokens:
		if token == "..":
			if len(stack) == 0 or stack[-1] == token:
				stack.append(token)
			elif stack[-1] != "":
				stack.pop()
			elif stack[-1] == "":
				continue
		else:
			stack.append(token)
	
	if len(stack) == 1 and stack[0] == "":
		return "/"
	return "/".join(stack)

def isValid(token):
	return len(token) > 0 and token != "."
