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
        curr = head
        memo = None
        while True: # 1 -> 2 -> 3 -> 4 -> 5 -> None
            c_next = curr.next  # 2 -> 3
            curr.next = memo
            memo = curr
            if not c_next:
                break
            curr = c_next
        return curr

h5 = ListNode(5)
h4 = ListNode(4, h5)
h3 = ListNode(3, h4)
h2 = ListNode(2, h3)
h1 = ListNode(1, h2)

sol = Solution()
curr = sol.reverseList(h1)

while True:
    print(curr.val)
    if curr.next is None:
        break
    curr = curr.next