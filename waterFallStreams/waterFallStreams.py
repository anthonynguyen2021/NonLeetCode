# Time = O(w^2h) | Space = O(w)
def waterfallStreams(array, source):
    	aboveRow = array[0][:]
	aboveRow[source] = -100
	
	for row in range(1, len(array)):
		currentRow = array[row][:]
		
		for idx in range(len(aboveRow)):
			hasWaterAbove = aboveRow[idx] < 0
			hasSolid = currentRow[idx] == 1
			
			if not hasWaterAbove:
				continue
			
			if not hasSolid:
				currentRow[idx] += aboveRow[idx]
				continue
			
			splitWaterVal = aboveRow[idx] / 2
			
			rightIdx = idx
			while rightIdx + 1 < len(aboveRow):
				rightIdx += 1
				if aboveRow[rightIdx] == 1:
					break
				if currentRow[rightIdx] != 1:
					currentRow[rightIdx] += splitWaterVal
					break
			leftIdx = idx
			while leftIdx-1 >= 0:
				leftIdx -= 1
				if aboveRow[leftIdx] == 1:
					break
				if currentRow[leftIdx] != 1:
					currentRow[leftIdx] += splitWaterVal
					break
		aboveRow = currentRow
	return list(map(lambda x : -x, aboveRow))
