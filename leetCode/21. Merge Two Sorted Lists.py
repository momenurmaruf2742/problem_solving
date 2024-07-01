from tkinter.tix import ListNoteBook
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNoteBook], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=sorted(list1)
        list4=sorted(list2)
        return list3.extend(list4)


a=Solution
print(a.mergeTwoLists(None,[1,2,4],[1,3,4]))