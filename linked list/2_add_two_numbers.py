# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        
        dummy = ListNode(-1)
        ptr = dummy
        carry = 0

        while ptr1 or ptr2:
            if ptr1 and ptr2:
                carry =  carry + ptr1.val + ptr2.val
            elif ptr1:
                carry =  carry + ptr1.val
            else:
                carry =  carry + ptr2.val
            node = carry % 10
            ptr.next = ListNode(node)

            ptr = ptr.next
            carry //= 10

            if ptr1: ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next

        if carry:
            ptr.next = ListNode(carry)

        return dummy.next
