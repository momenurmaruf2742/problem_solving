# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=0
        new_l2=[]
        for i in l1:
            s=str(l1[i]+l2[i])+str(d)
            if len(s)>1:
                ss=str(d)
                ss+=s[0]
                new_l2.append(s[1])
        print(new_l2)
a=Solution
a.addTwoNumbers(None,[1,2,4],[1,3,4])