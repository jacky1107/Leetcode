def solution(A, B):
    graph = {}
    for i in range(len(A)):
        if A[i] not in graph: graph[A[i]] = []
        if B[i] not in graph: graph[B[i]] = []
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    count = 0
    start_node = 0
    visited = [start_node]
    nodes = graph[start_node]
    for node in nodes:
        l = []
        dfs(graph, node, visited, l)
        count += (len(l) // 5) + 1
    print(count)

def dfs(graph, node, visited, l):
    if node in visited: return []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if len(graph[neighbor]) == 1: l.append(neighbor)
            dfs(graph, neighbor, visited, l)

A = [1,1,1,9,9,9,9,7,8]
B = [2,0,3,1,6,5,4,0,0]
solution(A, B)