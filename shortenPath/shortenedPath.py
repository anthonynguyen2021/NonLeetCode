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
