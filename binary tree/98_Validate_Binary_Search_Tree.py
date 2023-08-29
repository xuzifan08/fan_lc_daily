# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(float('-inf'), root, float('inf'))]

        while stack:
            small, node, big = stack.pop()

            if not(small < node.val < big):
                return False

            if node.left:
                stack.append((small,node.left,node.val))
            if node.right:
                stack.append((node.val, node.right, big))

        return True