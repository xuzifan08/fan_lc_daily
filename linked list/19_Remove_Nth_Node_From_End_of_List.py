# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-1, head)

        ptr1 = dummy
        ptr2 = dummy

        for i in range(n):
            ptr1 = ptr1.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return dummy.next
    

    #         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n ==1:
            return None
        
        # 
        # dummy -> 1 -> 2 
        #               ptr
        #. curr 

        dummy = ListNode(-1, head)
        ptr = dummy

        for i in range(n):
            ptr = ptr.next


        curr = dummy

        while ptr.next:
            ptr = ptr.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next