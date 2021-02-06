# Idea: Use recursion where we keep track of where we're at in phoneNumber and at each character in the phoneNumber
# We build up the string by looking at the string associated with each number. When the index of where we're at 
# in the phonenumber is equal to len(phonenumber), we append and return the function.

# Time = O(n * 4^n) - 4^n because we visited all 4^n possible strings and appending string of length n so the copying takes that long
# Space = O(n * 4^n) - 4^n is all possible strings in the worst case with length n
def phoneNumberMnemonics(phoneNumber):
    phoneBook = {'1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0'}
	result = []
	buildMnemonics(phoneNumber, phoneBook, result, 0, "")
	return result
	
def buildMnemonics(phoneNumber, phoneBook, result, i, currentString):
	if i == len(phoneNumber):
		result.append(currentString)
		return
	for j in phoneBook[phoneNumber[i]]:
		buildMnemonics(phoneNumber, phoneBook, result, i+1, currentString + j)
	return
