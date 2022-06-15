
def dfs(node, adjacency, visited):
    if node in visited:
        return False
    visited.append(node)
    for neighbor in adjacency[node]:
        dfs(neighbor, adjacency, visited)
    return True


def connect_components(adjacency):
    count = 0
    visited = []
    for node, _ in adjacency.items():
        if dfs(node, adjacency, visited):
            count += 1
    return count

adjacency = {
    0: [1, 5, 8],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}
count = connect_components(adjacency)
print(count)