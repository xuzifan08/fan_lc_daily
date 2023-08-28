# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([(root)])
        zigzag = False
        res = []

        while queue:
            level_len = len(queue)
            level = []

            for i in range(level_len):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if zigzag:
                res.append(level[::-1])
            else:
                res.append(level)

            zigzag = not zigzag

        return res


