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
