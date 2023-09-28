class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy ->  2 -> 3 -> 3 -> 3 -> 4 -> 4 -> 5
        #.        prev  curr
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next