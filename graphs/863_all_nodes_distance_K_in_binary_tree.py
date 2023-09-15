# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # turning a tree to a undirected gragh
        def dfs(node, parent):
            if not node:
                return

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        seen = {target}
        queue = deque([target])
        distance = 0

        while queue and distance < k:
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1

        return [node.val for node in queue]


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first turn it into a undirected graph
        def dfs(node, parent):
            if not node:
                return None

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right,node)
        
        dfs(root, None)


        seen = {target}
        queue = deque([(target, 0)])

        output = []

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                output.append(node.val)
            if distance > k:
                break
            for nei in [node.left, node.right, node.parent]:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, distance + 1))


        return output 