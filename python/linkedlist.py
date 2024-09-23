
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node = TreeNode(3)
node.next = TreeNode(3)
node.next.next = TreeNode(3)
node.next.next.next = TreeNode(3)
node.next.next.next.next  = TreeNode(11)
node.next.next.next.next.next  = TreeNode(2)
node.next.next.next.next.next.next  = TreeNode(22)

def removeDuplicates(llist):
    # Write your code here
    
    head = llist
    while head:
        if head.next and head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
            
    return llist

removeDuplicates(node)
print()

head = node
while head:
    print(head.data)
    head = head.next
        