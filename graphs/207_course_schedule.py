class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visited_set = set()

        def dfs(course):
            if course in visited_set:
                return False
            if pre_map[course] == []:
                return True

            visited_set.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visited_set.remove(course)
            pre_map[course] = []
            return True



        for course in range(numCourses):
            if not dfs(course): return False

        return True
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):return False
            visited.remove(crs)
            pre_map[crs] = []
            return True


        
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_map[crs] = []
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_crs = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_crs[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if pre_crs[crs] == []:
                return True

            visited.add(crs)
            for pre in pre_crs[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_crs[crs] = []
            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_crs = collections.defaultdict(list)

        for crs, pre in prerequisites:
            pre_crs[crs].append(pre)

        seen = set()
        
        def dfs(crs):
            if pre_crs[crs] == []:
                return True
            if crs in seen:
                return False

            seen.add(crs)

            for pre in pre_crs[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            pre_crs[crs] = []
            return True# if we can finish this crs



        for i in range(numCourses):
            if not dfs(i):
                return False


        return True