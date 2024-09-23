from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeComplex(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length = len(postorder)
        if length == 0: return None
        
        root = postorder[-1]
        for i in range(length):
            if inorder[i] == root: index = i

        node = TreeNode(root)

        left_inorder = []
        left_postorder = []
        for i in range(index):
            left_inorder.append(inorder[i])
            left_postorder.append(postorder[i])
        
        right_inorder = []
        right_postorder = []
        for i in range(index+1, len(postorder)):
            right_inorder.append(inorder[i])
        for i in range(index, len(postorder)-1):
            right_postorder.append(postorder[i])

        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            node = TreeNode(postorder[-1])
            index = inorder.index(node.val)
            node.left = self.buildTree(inorder[:index], postorder[:index])
            node.right = self.buildTree(inorder[index+1:], postorder[index:len(postorder)-1])
            return node

def print_tree(tree):
    if tree is not None:
        print(tree.val)
        print_tree(tree.left)
        print_tree(tree.right)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol = Solution()
res = sol.buildTree(inorder, postorder)
print_tree(res)
