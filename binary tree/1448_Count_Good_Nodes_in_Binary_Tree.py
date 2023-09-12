class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # store the maximum value 
        stack = [(root, root.val)]
        num_good = 1

        while stack:
            node, max_val = stack.pop()
            if node.left:
                if node.left.val >= max_val:
                    num_good += 1
                stack.append((node.left, max(node.left.val, max_val)))
            if node.right:
                if node.right.val >= max_val:
                    num_good += 1
                stack.append((node.right, max(node.right.val, max_val)))

        return num_good
    

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            if node.val >= max_so_far:
                res = 1
            else:
                res = 0

            res += dfs(node.left, max(node.val, max_so_far))
            res += dfs(node.right, max(node.val, max_so_far))

            return res

        return dfs(root, float('-inf'))
