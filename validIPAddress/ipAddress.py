# Explanation of solution: For the for loops (nested), we are looping over variables i so that the first period is at string index i, so the substring from 0 to i-1 is the 
# first part of the ip address. The min is there so t hat i doesn't go to invalid string indices like len(string). After we pick i, the next period goes at position 
# j = i+1 to i+4 (or len(string) which ever is smaller)


# Time = O(1) | Space = O(1) 
def validIPAddresses(string):
	# Output of our answer
	listOfIpAddress = []

	for i in range(1, min(len(string), 4)):

		buildIP = ['', '', '', '']
		buildIP[0] = string[:i]

		if not validString(buildIP[0]):
			continue
		
		for j in range(i + 1, min(len(string), i + 4)):

			buildIP[1] = string[i:j]

			if not validString(buildIP[1]):
				continue

			for k in range(j + 1, min(len(string), j + 4)):
				buildIP[2] = string[j:k]
				buildIP[3] = string[k:]
				if validString(buildIP[2]) and validString(buildIP[3]):
					listOfIpAddress.append('.'.join(buildIP))

	return listOfIpAddress


def validString(string):
	intOfString = int(string)
	if intOfString > 255:
		return False
	return len(string) == len(str(int(string)))  # Think string '0' and '00' where int('00') = 0


# Alternate way of defining validation of valid segment of IP address.
def validString(string):

	intOfString = int(string)

	if intOfString > 255:
		return False

	if len(string) == 0:
		return False

	if len(string) == 1:
		return True
	elif len(string) == 2:
		if string[0] == '0':
			return False
		else:
			return True
	elif len(string) == 3:
		if string[0] == '0':
			return False
		else:
			return True
