graph = {100: set([67, 66]),
         67: set([100, 82, 63]),
         66: set([100, 73, 69]),
         82: set([67, 61, 79]),
         63: set([67]),
         73: set([66]),
         69: set([66, 65, 81]),
         61: set([82]),
         79: set([82, 87, 77]),
         65: set([69, 84, 99]),
         81: set([69]),
         87: set([79, 31, 78]),
         77: set([79]),
         84: set([65]),
         99: set([65]),
         31: set([87]),
         78: set([87])}


def MAX(graph, start):
    stack = [start]
    visit = []
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            nextGraph = graph[n] - set(visit)
            if len(nextGraph) == 0:
                visit += stack
                break
            stack.append(max(nextGraph))
    visit.pop(0)
    return visit


def MIN(graph, start):
    stack = [start]
    visit = []
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            nextGraph = graph[n] - set(visit)
            if len(nextGraph) == 0:
                visit += stack
                break
            stack.append(min(nextGraph))
    visit.pop(0)
    return visit


print("MAX : " + ''.join(map(chr, MAX(graph, 100))))
print("MIN : " + ''.join(map(chr, MIN(graph, 100))))
