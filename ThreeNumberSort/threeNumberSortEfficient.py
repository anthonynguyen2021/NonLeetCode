# Time = O(n)
# Space = O(1) 
# Idea of solution: Uses three pointers. The first points to the position where order[0] needs to go to. The second pointer checks if it's order[1], it just increments by one.
# If second pointer points to order[2], we swap it with the value of the third pointer's value, then decrement the third pointer (note we don't increment the second pointer
# as we don't know if the value corresponding to the second pointer is order[2] or order[0] or not). This solution is nice since it does 1 pass through the array. 

def threeNumberSort(array, order):
	first, second, third = 0, 0, len(array) - 1
	while second <= third:
		currentValue = array[second]
		
		if currentValue == order[1]:
			second += 1
		elif currentValue == order[0]:
			swap(array, first, second)
			first += 1
			second += 1
		else:
			swap(array, second, third)
			third -= 1
	return array
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
