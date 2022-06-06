hashMap = {
    "i": ['j', 'k'],
    "j": ['i'],
    "k": ['i', 'm', 'l'],
    "m": ['k'],
    "l": ['k'],
    "o": ['n'],
    "n": ['o'],
}

visited = []
def hasPath(graph, start, end):
    if start == end: return True
    if start in visited: return False
    visited.append(start)
    print(start)
    for neighbor in graph[start]:
        if hasPath(graph, neighbor, end):
            print(neighbor)
            return True

    return False

res = hasPath(hashMap, "i", "l")
print(res)