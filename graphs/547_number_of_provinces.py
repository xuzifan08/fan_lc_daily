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
    

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build a graph as a hashmap with node and it's neighbors
        city = collections.defaultdict(list)
        row = len(isConnected)
        col = len(isConnected[0])

        for r in range(row):
            for c in range(r+1, col):
                if isConnected[r][c] == 1:
                    city[r].append(c)
                    city[c].append(r)
        

        visited_city = set()

        def dfs(c):
            for nei in city[c]:
                if nei not in visited_city:
                    visited_city.add(nei)
                    dfs(nei)


        province = 0

        for i in range(len(isConnected)):
            if i not in visited_city:
                province += 1
                visited_city.add(i)
                dfs(i)

        return province