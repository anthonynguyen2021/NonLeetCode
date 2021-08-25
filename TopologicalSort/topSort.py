# T = S = O(v + e)
# build graph and return top ordering
def topologicalSort(jobs, deps):
    graph = CreateGraph(jobs, deps)
	return getTopOrder(graph)

# Build graph and add prerequisites
def CreateGraph(jobs, deps):
	graph = JobGraph(jobs)
	for prereq, job in deps:
		graph.addPrerequisite(job, prereq)
	return graph

# Take nodes in graph.nodes, as long as it's not empty, pop out and dfs on that node
# Not usual iterative or recursive dfs as in appending.
def getTopOrder(graph):
	nodes = graph.nodes
	topOrder = []
	while len(nodes) > 0:
		node = nodes.pop()
		isCycle = depthFirstSearch(node, topOrder)
		if isCycle:
			return []
	return topOrder

# If visited, we have went to this node. If visiting, we encountered a cycle. A topological sorting rely
# on no cycle. Backtrack with node.visiting set to True then False. We look at neighbor of node, if
# there's a cycle on neighbor, return True. Once we backtrack to node.visiting = False, we're done
# visiting node, so set node.visited = True. We went through the prerequisites of node, we append node.job
def depthFirstSearch(node, topOrder):
	if node.visited:
		return False
	if node.visiting:
		return True # hit a cycle
	node.visiting = True
	for neighbor in node.prereq:
		if depthFirstSearch(neighbor, topOrder):
			return True
	node.visiting = False
	node.visited = True
	topOrder.append(node.job)
	return False

# create directed graph
# Initialized with nodes: List[JobNode], graph[int] = JobNode, and add nodes for each job in jobs
# 3 methods - add nodes, get nodes, addPrereqisites
class JobGraph:
	def __init__(self, jobs):
		self.nodes = [] # List[JobNode]
		self.graph = {} # int -> JobNode
		for job in jobs:
			self.addNode(job)
		
	def addNode(self, job):
		if job not in self.graph:
			self.graph[job] = JobNode(job)
		self.nodes.append(self.graph[job])
		
	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
		return self.graph[job]
	
	def addPrerequisite(self, job, prerequisite):
		jobNode = self.getNode(job)
		prereqNode = self.getNode(prerequisite)
		jobNode.prereq.append(prereqNode)
	
# Job node with attribute job, prereq: List[JobNode], visited - used for DFS, visiting - track visiting
# in a current stack - detect cycle. 
class JobNode:
	def __init__(self, job):
		self.job = job # int
		self.prereq = [] # List[JobNode]
		self.visited = False
		self.visiting = False
