class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            if not node.left and not node.right:
                return targetSum == curr + node.val

            curr += node.val 
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right
        return dfs(root, 0)
