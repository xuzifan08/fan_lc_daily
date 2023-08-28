# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]


        while stack:

            root, curr_sum = stack.pop()

            if root is not None:
                curr_sum = curr_sum*10+root.val

            if not root.left and not root.right:
                root_to_leaf += curr_sum

            if root.left:
                stack.append((root.left, curr_sum))
            if root.right:
                stack.append((root.right, curr_sum))

        return root_to_leaf

        