# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        
        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return True

        deq = collections.deque([(p, q), ])

        while deq:
            p, q = deq.popleft()
            
            if not check(p, q):
                return False

            if p.left and q.left:
                deq.append((p.left, q.left))
            elif p.left or q.left:
                return False
            if p.right and q.right:
                deq.append((p.right, q.right))
            elif p.right or q.right:
                return False
        return True
    

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)