# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return



n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)


sol = Solution()
curr = sol.reverseList(n1)


head = curr
while True:
    print(head.val)
    if head.next is None:
        break
    head = head.next
