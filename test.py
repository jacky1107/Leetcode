class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(2)
node.left = TreeNode(0)
node.right = TreeNode(3)
node.right.left = TreeNode(0)
node.right.right = TreeNode(1)

class Solution:
    def evaluateTree(self, root) -> bool:
        if not root: return False
        return self.dfs(root)

    def dfs(self, root):
        if not root.left and not root.right: return root.val
        if root.val == 2:
            return self.dfs(root.left) | self.dfs(root.right)
        if root.val == 3:
            return self.dfs(root.left) & self.dfs(root.right)

sol = Solution()
re = sol.evaluateTree(node)
print(re)
