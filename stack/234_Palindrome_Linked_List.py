# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # [1,2,2,1]
        #.         f
        #.     s 

        # [1,2,0,2,1]
        #.         f
        #.     s

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        stack = []

        while slow:
            stack.append(slow.val)
            slow = slow.next

        while stack:
            node = stack.pop()
            if node != head.val:
                return False
            head = head.next
        
        return True if not stack else False