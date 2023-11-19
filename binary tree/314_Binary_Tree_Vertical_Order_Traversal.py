class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([(root, 0)])
        hash_col = collections.defaultdict(list)

        while queue:
            node, col = queue.popleft()
            hash_col[col].append(node.val)
            if node.left:
                queue.append((node.left, col -1))
            if node.right:
                queue.append((node.right, col + 1))

        
        return [hash_col[x] for x in sorted(hash_col.keys())]