# Time = O(N) | Space = O(N)
def taskAssignment(k, tasks):
    indexTasks = [i for i in range(len(tasks))]
	indexTasks.sort(key = lambda x : tasks[x])
	taskAssignmentOptimal = []
	for idx in range(k):
		taskAssignmentOptimal.append([indexTasks[idx]])
	for idx in range(k):
		taskAssignmentOptimal[-idx-1].append(indexTasks[k+idx])
    return taskAssignmentOptimal
