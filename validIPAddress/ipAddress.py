# Time = O(1) | Space = O(1) 
def validIPAddresses(string):
	# Output of our answer
    listOfIpAddress = []
	for i in range(1, min(len(string), 4)):
		buildIP = ['', '', '', '']
		buildIP[0] = string[:i]
		if not validString(buildIP[0]):
			continue
		
		for j in range(i+1, min(len(string), i+4)):
			buildIP[1] = string[i:j]
			if not validString(buildIP[1]):
				continue
			for k in range(j+1, min(len(string), j+4)):
				buildIP[2] = string[j:k]
				buildIP[3] = string[k:]
				if validString(buildIP[2]) and validString(buildIP[3]):
					listOfIpAddress.append('.'.join(buildIP))
	return listOfIpAddress

def validString(string):
	intOfString = int(string)
	if intOfString > 255:
		return False
	return len(string) == len(str(int(string)))
