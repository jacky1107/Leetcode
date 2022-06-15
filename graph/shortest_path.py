def buildGraph(edges):
    graph = {}
    for (a, b) in edges:
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def shortest_path(edges, start_node, end_node):
    graph = buildGraph(edges)
    distance = 0
    visited = []
    queue = [(start_node, distance)]
    while len(queue) > 0:
        node, distance = queue[0]
        if node == end_node:
            return distance
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
        queue = queue[1:]
    return -1

edges = [
    ["w", "x"],
    ["x", "y"],
    ["y", "o"],
    ["o", "z"],
    ["w", "v"],
    ["v", "i"],
    ["i", "p"],
    ["p", "z"],
]
print(shortest_path(edges, "w", "z")) # 4

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
print(shortest_path(edges, "w", "z"))

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
print(shortest_path(edges, "y", "x"))

edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
print(shortest_path(edges, "a", "e"))

edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
print(shortest_path(edges, "e", "c"))

edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
print(shortest_path(edges, "b", "g"))


edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]
print(shortest_path(edges, "w", "e"))

edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]
print(shortest_path(edges, "n", "e"))

edges = [
    ['m', 'n'],
    ['n', 'o'],
    ['o', 'p'],
    ['p', 'q'],
    ['t', 'o'],
    ['r', 'q'],
    ['r', 's']
]
print(shortest_path(edges, "m", "s"))
