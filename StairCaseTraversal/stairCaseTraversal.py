def staircaseTraversal(height, maxSteps):
    heightSolution = [0 for _ in range(0, height + 1)]
	heightSolution[0] = 1
	heightSolution[1] = 1
	
	for currentHeight in range(2, len(heightSolution)):
		currentStep = 1
		while currentStep <= maxSteps and currentStep <= currentHeight:
			heightSolution[currentHeight] += heightSolution[currentHeight - currentStep]
			currentStep += 1
	return heightSolution[-1]
