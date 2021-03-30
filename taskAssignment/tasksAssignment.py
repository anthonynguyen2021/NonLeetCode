# Explanation: The idea is that if we view k employees as the following: If the person who completes the task in the shortest amount of task (there exists
# at least 1), then that person should finish a task that takes the longest to save everyone else time. This is just 1 person. We iterate the same logic 
# for the remaining 2k-2 tasks and k-1 people. Since the prompt asks us to locate the indices, not the tasks the taking the least, ... , longest, we sort
# by indices where we pass the key = lambda x : array[x]. The first and last goes to the first person. The second and second to the last goes the 2nd. And
# so on.

# Explanation of complexities: The time comes from the for loop and sorting. The space comes from index Tasks.
# Time = O(NlogN) | Space = O(N)
def taskAssignment(k, tasks):
    	indexTasks = [i for i in range(len(tasks))]
	indexTasks.sort(key = lambda x : tasks[x])
	taskAssignmentOptimal = []
	for idx in range(k):
		taskAssignmentOptimal.append([indexTasks[idx]])
	for idx in range(k):
		taskAssignmentOptimal[-idx-1].append(indexTasks[k+idx])
    return taskAssignmentOptimal

# Idea of 2nd solution: For each task length in array, we create a hash map that maps the task length to its indices in array. We do that for all elements 
# of array. Then we sort the array and call it sortedArray. Then we iterate through the sorted Array and look at its first and last element with respect
# to the hash element, we have two indices and make sure to pop those from the hashMap[first] and hashMap[last]. Append this to our solution. Then
# we go thorugh the 2nd and 2nd to last, and do the same and so on. This solution has the same complexity as the solution above.
