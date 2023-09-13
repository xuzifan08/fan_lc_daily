class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_map[course].append(pre)
    
        visited, cycle = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()
        cycle = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True




        for c in range(numCourses):
            if not dfs(c):
                return []
        return output