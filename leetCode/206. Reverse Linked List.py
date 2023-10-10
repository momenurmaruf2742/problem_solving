from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head.reverse()
        return head

a=Solution
print(a.reverseList(None,[1,2,3,4,5,6]))