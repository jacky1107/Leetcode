from typing import List
import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        table = [i for i in range(len(edges)+1)]
        print(table)

        def find(node):
            if node != table[node]:
                print(node, table[node], find(table[node]))
                table[node] = find(table[node])
            return table[node]

        def update(s, e):
            table[find(e)] = find(s)

        for s, e in edges:
            print(table, s, e)
            if find(s) == find(e):
                print(table, s, e)
                return [s, e]
            else: update(s, e)

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
edges = [[2,3],[1,2],[1,3]]
sol = Solution()
print(sol.findRedundantConnection(edges))
