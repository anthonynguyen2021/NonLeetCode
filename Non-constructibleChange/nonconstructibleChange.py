

# Time = O(nlogn) where n is the length of the input array and we used an in place sorting algorithm
# Space = O(1)

def nonConstructibleChange(coins):
	coins.sort()
	change = 0
	for idx in range(len(coins)):
		value = coins[idx]
		if value > change+1:
			return change+1
		change += value
	return change+1
