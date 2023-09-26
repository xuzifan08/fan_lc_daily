"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                if i < length - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
    


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = collections.deque([(root)])

        while q:
            num_level = len(q)
            
            for i in range(num_level):
                node = q.popleft()
                if i + 1 < num_level:
                    node.next = q[0]
                else:
                    node.next = None

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
    

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None


        queue = collections.deque([root])

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                if i + 1 == level_length:
                    node.next = None
                else:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root