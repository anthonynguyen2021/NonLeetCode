# Time O(n) - 2 for loops (non-nested)
# Space O(n) - product array - using just auxillary array of size n
# Idea is to get a running product to the left and right of index idx. We initialize an array with 1s.
# We populate the left running product first with a for loop. Next, we keep track of a right running product
# from index len(array)-1, ... , 0 and multiply it to prod[idx].
def arrayOfProducts(array):
	if len(array) == 1:
		return array
    product = [1 for _ in array]
	leftRunningProd = 1
	for idx in range(len(array)):
		product[idx] = leftRunningProd
		leftRunningProd *= array[idx]
	
	rightRunningProd = 1
	for idx in reversed(range(len(array))):
		product[idx] *= rightRunningProd
		rightRunningProd *= array[idx]
		
	return product
