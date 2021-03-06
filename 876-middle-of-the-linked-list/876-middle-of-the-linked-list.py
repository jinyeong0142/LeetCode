# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import ceil

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        cur = head
        
        while cur.next is not None:
            length += 1
            cur = cur.next
        
        cur = head
        
        for i in range(ceil(length/2)):
            cur = cur.next
        
        return cur