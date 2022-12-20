

# Time = O(n)
# Space = O(n) 
# Issue: We have two auxillary array of size n. Can we do better?
def arrayOfProducts(array):

	if len(array) == 1:
		return array

	leftRunningSum = [1 for _ in array]
	rightRunningSum = [1 for _ in array]

	for idx in range(1, len(array)):
		leftRunningSum[idx] = leftRunningSum[idx - 1] * array[idx - 1]

	for idx in reversed(range(len(array) - 1)):
		rightRunningSum[idx] = rightRunningSum[idx + 1] * array[idx + 1]

	return [leftRunningSum[i] * rightRunningSum[i] for i in range(len(array))]
