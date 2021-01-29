# Time = O(n^2) - two forloops 
# Space = O(n) - storage for the output
def arrayOfProducts(array):
	output = array[:]
	for i in range(len(array)):
		currentProduct = 1
		for j in range(len(array)):
			if i != j:
				currentProduct *= array[j]
		output[i] = currentProduct 
	return output 
