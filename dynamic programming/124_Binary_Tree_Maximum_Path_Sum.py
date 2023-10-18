class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            res[0] = max(res[0], root.val + left_max + right_max)

            return max(left_max, right_max) + root.val
        dfs(root)
        return res[0]