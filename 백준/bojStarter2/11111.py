from collections import deque
from math import inf
from sys import stdin
input = stdin.readline


def hasPath(graph, costList, visited, start, end):
	n = len(graph)
	
	distList = [inf] * n
	distList[start] = 0
	inQueue = [False] * n
	inQueue[start] = True

	qu = deque([start])
	while qu:
		here = qu.popleft()
		inQueue[here] = False

		for there in graph[here]:
			if graph[here][there] > 0:
				newCost = distList[here] + costList[here][there]

				if newCost < distList[there]:
					distList[there] = newCost
					visited[there] = here

					if not inQueue[there]:
						qu.append(there)
						inQueue[there] = True

	return visited[end] != -1


# retutn minimum Cost, most minimum Cost, maximum Flow
def getMCMNCMF(graph, costList, source, sink) -> (int, int, int):
	n = len(graph)
	minCost, maxFlow = 0, 0
	minestCost = 0
	
	while True:
		visited = [-1] * n
		if not hasPath(
			graph, costList, visited, source, sink
		):
			break

		nowFlow = inf

		here = sink
		while here != source:
			there = visited[here]
			nowFlow = min(
				nowFlow, graph[there][here]
			)
			here = there

		here = sink
		while here != source:
			there = visited[here]
			graph[there][here] -= nowFlow
			graph[here][there] += nowFlow
			minCost += costList[there][here] * nowFlow
			here = there

		minestCost = min(minestCost, minCost)
		maxFlow += nowFlow

	return minCost, minestCost, maxFlow


def solve():
	h, w = map(int, input().split())
	n = w * h + 2
	source, sink = n - 2, n - 1
	
	gradeToCost = [
		[10, 8, 7, 5, 1],
		[8, 6, 4, 3, 1],
		[7, 4, 3, 2, 1],
		[5, 3, 2, 2, 1],
		[1, 1, 1, 1, 0]
	]
	gradeList = [
		[
			{"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}[e]
			for e in input().strip()
		]
		for _ in range(h)
	]
	
	graph = [dict() for _ in range(n)]
	costList = [[0] * n for _ in range(n)]
	
	def connect(node1, node2, flow, cost=inf):
		graph[node1][node2] = flow
		graph[node2][node1] = 0

		if cost != inf:
			costList[node1][node2] = cost
			costList[node2][node1] = -cost
	
	for yEven in range(h):
		for xEven in range(w):
			if (xEven + yEven) % 2:
				continue
			
			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				xOdd, yOdd = xEven + dx, yEven + dy
				if not (xOdd in range(w) and yOdd in range(h)):
					continue
				
				idxEven = yEven * w + xEven
				idxOdd = yOdd * w + xOdd
				connect(
					idxEven, idxOdd, 1,
					-gradeToCost[
						gradeList[yEven][xEven]
					][
						gradeList[yOdd][xOdd]
					]
				)
	
	for y in range(h):
		for x in range(w):
			idx = y * w + x
			
			if (x + y) % 2:
				connect(idx, sink, 1)
			else:
				connect(source, idx, 1)
	
	return -getMCMNCMF(graph, costList, source, sink)[1]

print(solve())