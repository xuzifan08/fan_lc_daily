# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left  

    def next(self) -> int:
        res = self.stack.pop()
        node = res.right

        while node:
            self.stack.append(node)
            node = node.left

        return res.val
        

    def hasNext(self) -> bool:
        return len(self.stack) != 0
    

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        node = res.right

        while node:
            self.stack.append(node)
            node = node.left

        return res.val
        
    def hasNext(self) -> bool:

        return len(self.stack)!=0
    

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        res = node.val
        node = node.right

        while node:
            self.stack.append(node)
            node = node.left
        return res
        
    def hasNext(self) -> bool:
        return len(self.stack)