def largest_components(graph):
    largest = 0
    visited = []
    for node, _ in graph.items():
        size = depth_searching(graph, node, visited)
        if size > largest: largest = size
    return largest


def depth_searching(graph, node, visited):
    if node in visited: return 0
    visited.append(node)
    size = 1
    for neighbor in graph[node]:
        size += depth_searching(graph, neighbor, visited)
    return size

graph = {
    0: [1, 5, 8],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}


count = largest_components(graph)
print(count)