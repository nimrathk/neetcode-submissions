# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# do i create new nodes & assign values to them
# or do i somehow reassign the pointers
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None

        l1 = list1
        l2 = list2
        
        if l1.val <= l2.val:
            dummy = l1
            l1 = l1.next
        else:
            dummy = l2
            l2 = l2.next
        
        curr = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2

        return dummy