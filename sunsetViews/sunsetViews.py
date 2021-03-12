# Time = O(n)
# Space = O(n)
def sunsetViews(buildings, direction):
	return sunsetBuildingsIdx(buildings, direction)

def sunsetBuildingsIdx(buildings, direction):
	largestHeightSeen = 0
	buildingListIdx = []
	if direction == "WEST":
		for idx in range(len(buildings)):
			if buildings[idx] > largestHeightSeen:
				buildingListIdx.append(idx)
				largestHeightSeen = buildings[idx]
	else:
		for idx in reversed(range(len(buildings))):
			if buildings[idx] > largestHeightSeen:
				buildingListIdx.append(idx)
				largestHeightSeen = buildings[idx]
		buildingListIdx = buildingListIdx[::-1]
	return buildingListIdx
