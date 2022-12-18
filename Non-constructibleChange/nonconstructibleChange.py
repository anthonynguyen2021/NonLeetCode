

def nonConstructibleChange(coins):
	'''
	Idea of Solution:
	
	Suppose the array is sorted. We can solve this by dynamic programming. Assume that coins[0], ..., coins[i], we make make change up do value "change".
	So the solution to this subarray is change+1. If value = coins[i+1] > change + 1, we can't make a change of value "change + 1". If we use the coin coins[i+1], 
	this is more than change + 1. If we don't, we can make change up to "change". Therefore, we return "change + 1". Otherwise, we assume value = coins[i+1] <= change + 1. 
	Since we can make change up to {1, ..., change} and value <= change + 1, we can make change up to coins[i+1] + change because we can make 
	additional change {coins[i+1], coins[i+1] + 1, ...., coins[i+1] + change}. Therefore, we can make change up to value + change. So we return value + change + 1. 

	Time = O(nlogn) where n is the length of the input array and we used an in place sorting algorithm
	Space = O(1)
	'''
	coins.sort()
	change = 0

	for idx in range(len(coins)):

		value = coins[idx]

		if value > change + 1:
			return change + 1

		change += value

	return change + 1
