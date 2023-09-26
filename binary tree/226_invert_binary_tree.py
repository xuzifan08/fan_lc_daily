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


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]


        while stack:
            node = stack.pop()

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


        return root
    


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root