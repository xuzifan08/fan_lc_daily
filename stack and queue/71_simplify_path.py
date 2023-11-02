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


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        print(path_list)
        stack = []

        for ele in path_list:
            if ele == '.' or ele == '':
                continue
            elif ele == '..' and stack:
                stack.pop()
            elif ele == '..' and not stack: continue
            else:
                stack.append(ele)
        print(stack)
        return '/' + '/'.join(stack)