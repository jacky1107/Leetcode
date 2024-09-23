
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root: return []
        temp = [{
            "level": 0,
            "root": root
        }]
        
        res = {}
        while len(temp) > 0:
            info = temp.pop()
            level = info["level"]
            node = info["root"]

            res.setdefault(level, [])
            res[level].append(node.val)

            if node.left: temp.append({"level": level + 1, "root": node.left})
            if node.right: temp.append({"level": level + 1, "root": node.right})

        return [v for _, v in res.items()]

    def connect(self, root):
        if not root: return []
        temp = [
            {
                "level": 0,
                "root": root
            }
        ]

        res = {}
        while len(temp) > 0:
            info = temp.pop()
            level = info["level"]
            node = info["root"]

            res.setdefault(level, [])
            res[level].append(node.val)
            if node.right: temp.append({"level": level+1, "root": node.right})
            if node.left: temp.append({"level": level+1, "root": node.left})

        result = []
        for _, v in res.items():
            v.append(None)
            result.extend(v)
        
        return result

node = TreeNode(3)

node.left = TreeNode(9)
node.left.left = TreeNode(11)
node.left.right = TreeNode(12)

node.right = TreeNode(20)

node.right.left = TreeNode(15)
node.right.right = TreeNode(7)


sol = Solution()
print(sol.connect(node))


while node:
    print(node.val)
    node = node.left

def deleteNode(llist, position):
    
    if llist is None:
        return

    count = 0
    head = llist
    
    while head.next and count < position:
        prev = head
        head = head.next
        count += 1
    
    if count == 0:
        llist = llist.next
    else:
        prev.next = head.next
        
    return llist