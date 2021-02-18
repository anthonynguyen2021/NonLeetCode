# Idea of solution: We sort both arrays. With no loss in generality, we may assume the back row are blue shirt students. If such a solution exists, we can find such 
# photo arrangements. Suppose we sorted our two input arrays. We will prove that it sufficeds to show that b_i > r_i for all i. Let redShirtHeights = [r_1, ...., r_n] 
# & blueShirtHeights = [b_1, ..., b_n]. By existence of solution, we may assume there exists a permutation (bijective) function f, so that r_f(i) < b_f(i).
# Note that b_n > a_i for some i. Also, note that for some k, we have b_k > a_n. Since these input arrays are sorted, we can rearrange these 4 students so that b_n > a_n 
# due to b_k > a_n and b_k > a_i since b_k > a_n. By induction, the results hold. 

# The pairings in the above explanation can be viewed as a bipartite graph where exactly 1 node from first set connects to exactly 1 node in the second set; in other words,
# each vertex has degree 1.

# Time = O(nlogn) 
# Space = O(1)

def classPhotos(redShirtHeights, blueShirtHeights):
  	redShirtHeights.sort()
	blueShirtHeights.sort()
	blueLargest = False
	if blueShirtHeights[-1] > redShirtHeights[-1]:
		blueLargest = True
	if blueLargest:
		for idx in reversed(range(len(blueShirtHeights))):
			if blueShirtHeights[idx] <= redShirtHeights[idx]:
				return False
	else:
		for idx in reversed(range(len(redShirtHeights))):
			if redShirtHeights[idx] <= blueShirtHeights[idx]:
				return False
	return True
