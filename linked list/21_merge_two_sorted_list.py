class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        head = dummy

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        elif l2:
            head.next = l2

        return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        head = dummy

        ptr1 = list1 
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val >= ptr2.val:
                head.next = ptr2
                ptr2 = ptr2.next
            else:
                head.next = ptr1
                ptr1 = ptr1.next
            head = head.next

        if ptr1:
            head.next = ptr1
        if ptr2:
            head.next = ptr2

        return dummy.next
