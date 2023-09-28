class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        #  dummy -> 1 -> 2 -> 3 -> 4 -> 5
        #                              prev
        #                    curr        

        dummy = ListNode(-1, head)
        count = 0
        ptr = dummy


        while ptr.next:
            count += 1
            ptr = ptr.next

        rotate = k % count

        prev = dummy

        for i in range(rotate):
            prev = prev.next

        curr = dummy

        while prev.next:
            curr = curr.next
            prev = prev.next

        prev.next = dummy.next
        dummy.next = curr.next
        curr.next = None


        return dummy.next