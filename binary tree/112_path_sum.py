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


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return not targetSum - root.val


        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)