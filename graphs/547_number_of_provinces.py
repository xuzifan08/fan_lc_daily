class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build a graph with hashmapp
        graph = collections.defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()

        # dfs basic funtion
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        province = 0
        # iterate through the nodes and dfs to count the provinces
        for i in range(len(isConnected)):
            if i not in seen:
                province += 1
                dfs(i)
        return province
    
# 2023.07.17
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = collections.defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            for neigbhor in graph[node]:
                if neigbhor not in seen:
                    seen.add(neigbhor)
                    dfs(neigbhor)

        seen = set()
        province = 0

        for i in range(n):
            if i not in seen:
                province += 1
                seen.add(i)
                dfs(i)

        return province