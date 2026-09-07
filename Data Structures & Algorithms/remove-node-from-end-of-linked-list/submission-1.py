# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        
        dummy = ListNode(0, head)
        p1 = dummy
        p2 = head

        i = 0
        while p2 and i < n:
            p2 = p2.next
            i += 1
        
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next

        return dummy.next
        