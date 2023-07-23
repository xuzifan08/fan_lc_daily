class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = path.split('/')
        
        stack = []

        for i in path_stack:
            if i == "..":
                if stack:
                    stack.pop()

            elif i =='.' or not i:
                continue

            else:
                stack.append(i)

        return "/" + "/".join(stack)
