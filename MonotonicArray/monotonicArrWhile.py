# Time = O(n)
# Space = O(1)

# Solution: The idea is that we perform a while loop to see when the increasingness / decreasingness are violated or not. We return these bool markers increase or decrease. 
def isMonotonic(array):
    increase, decrease = True, True
	idx = 0
	while idx+1 < len(array) and array[idx] <= array[idx+1]:
		idx += 1
	if idx+1 < len(array):
		increase = False
	idx = 0
	while idx+1 < len(array) and array[idx] >= array[idx+1]:
		idx += 1
	if idx+1 < len(array):
		decrease = False
	return increase or decrease
