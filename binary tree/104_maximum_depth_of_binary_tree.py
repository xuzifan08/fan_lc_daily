class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        ans = 0
        # [9, 15, 7]
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans