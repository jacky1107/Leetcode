from asyncio.windows_events import NULL


string = "6+2*3*(1-2)"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(string, index, node):
    s = string[index]
    if s in "+-":
        node = TreeNode()
        node.left = string[index-1]
        node.right = s
        buildTree(string, index+1, node)

    elif s in "*/":
        node.left = string[index-1]
        node.right = s
        buildTree(string, index, node)

    elif s in "()":
        node.left = string[index-1]
        node.right = s
        buildTree(string, index, node)

    node = TreeNode()


index = 0
node = TreeNode()
while index < len(string):
    index = buildTree(string, index, node)
    index += 1