# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # -1 -> 1 -> <- 2 <- 3  <- 4    5
       #. dummy lh                    curr
       # dummy is for setting the left_Head to store the previous node of the reverse nodes 
       # before starts reversing, save left_Head to another point
        if not head:return None
        dummy = ListNode(-1, head)
        left_head = dummy
        curr = head

        for i in range(left-1):
            curr = curr.next
            left_head = left_head.next

        prev = left_head

        for j in range(right - left + 1):
            nxt = curr.next 
            curr.next = prev
            
            prev = curr
            curr = nxt
        left_head.next.next = curr
        left_head.next = prev

        return dummy.next

