
def connect_components(node, adjacency):
    if node in visited:
        return False
    visited.append(node)
    for neighbor in adjacency[node]:
        connect_components(neighbor, adjacency)
    return True

adjacency = {
    0: [1, 5, 8],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

count = 0
visited = []
for node, neighbors in adjacency.items():
    if connect_components(node, adjacency):
        count += 1
print(count)