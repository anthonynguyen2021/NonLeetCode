# Time = O(n^2) | Space = O(1)
def validStartingCity(distances, fuel, mpg):
	for i in range(len(distances)):
		currentMilesToDrive = 0
		for j in range(len(distances)):
			currentMilesToDrive += mpg * fuel[(i+j) % len(fuel)] - distances[(i+j) % len(distances)]
			if currentMilesToDrive < 0:
				break
			if j == len(distances)-1:
				return i
