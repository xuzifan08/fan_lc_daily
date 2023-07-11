class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None


        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp 

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root