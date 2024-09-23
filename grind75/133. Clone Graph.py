from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        visited = {}

        def dfs(node):
            print(node.val)
            if node in visited:
                return visited[node]

            new_node = Node(node.val)
            visited[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node) if node else None
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)

node2.neighbors.append(node1)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
node4.neighbors.append(node3)

sol = Solution()
res = sol.cloneGraph(node1)

def print_node(node):

    visited = []
    queue = [node]
    while len(queue) > 0:
        node = queue[0]
        print(node.val)
        if node not in visited:
            queue.extend(node.neighbors)
            visited.append(node)

        queue = queue[1:]

print_node(res)