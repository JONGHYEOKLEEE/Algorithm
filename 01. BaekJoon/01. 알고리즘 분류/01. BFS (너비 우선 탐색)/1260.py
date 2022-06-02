from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    nodeA, nodeB = map(int, input().split())

    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

    graph[nodeA].sort()
    graph[nodeB].sort()

visitedDSF = [False] * (n + 1)

def DSF(graph, v):
    visitedDSF[v] = True

    print(v, end = " ")

    for x in graph[v]:
        if not visitedDSF[x]:
            DSF(graph, x)

def BSF(graph, v):
    visitedBSF = [False] * (n + 1)
    visitedBSF[v] = True

    deq = deque([v])

    while deq:
        pop = deq.popleft()

        print(pop, end = " ")
        
        for x in graph[pop]:
            if not visitedBSF[x]:
                visitedBSF[x] = True

                deq.append(x)

DSF(graph, v)
print()
BSF(graph, v)