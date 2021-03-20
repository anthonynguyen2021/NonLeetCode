# Explanation of solution: We solve this via DP. Sort the disk by their heights. We create heights array which has the same length as disks; at index i, we 
# Solve the problem of the largest disk heights total including disks[i]. Sequence stores the previous disk on top of disk[i] (after sorting). We 
# loop from disk 0, ..., len(disks) - 1; we check if heights[j] + 1 > heights[i], then we set heights[i] = heights[j]+1 and set sequence[i] = j for disk[j] to go on top of 
# disk i. We do this for j in range(0, i).

# Time = O(n^2) - follows from the two nested for loops; everything else is done in constant time. Note that sorting iss just O(nlogn)
# Space = O(n) - heights, sequences, and buildSequences are all O(n).
def diskStacking(disks):
	# We ask the interviewer if we need to make a copy of disks if we sort its 3rd element
	disks.sort(key = lambda disc : disc[2])
	heights = [disk[2] for disk in disks]  # Largest height so far
	sequence = [None for disc in disks]
	maxHeightIdx = 0
	for i in range(1, len(disks)):
		currentDisk = disks[i]
		for j in range(0, i):
			otherDisk = disks[j]
			if validDisk(otherDisk, currentDisk) and heights[i] < currentDisk[2] + heights[j]:
				heights[i] = currentDisk[2] + heights[j]
				sequence[i] = j
		if heights[i] > heights[maxHeightIdx]:
			maxHeightIdx = i
	return buildDiskSequence(disks, sequence, maxHeightIdx)
		
def validDisk(o, c):
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildDiskSequence(disks, sequence, idx):
	currentIdx = idx
	sequenceDisk = []
	while currentIdx != None:
		sequenceDisk.append(disks[currentIdx])
		currentIdx = sequence[currentIdx]
	return list(reversed(sequenceDisk))
				
				
