class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        neighbors = collections.defaultdict(list)

        for x, y in connections:
            roads.add((x, y))
            neighbors[x].append(y)
            neighbors[y].append(x)

        reroutes = 0
        seen = set()
        seen.add(0)

        def dfs(node):
            nonlocal reroutes
            for neighbor in neighbors[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        reroutes += 1
                    seen.add(neighbor)
                    dfs(neighbor)
        dfs(0)
        return reroutes