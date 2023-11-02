class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')',
                 '[': ']',
                 '{': '}'}

        stack = []

        for c in s:
            if c in check:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    prev = stack.pop()
                    if check[prev] != c:
                        return False

        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')',
                 '[': ']',
                 '{': '}'}

        stack = []
        
        for i in range(len(s)):
            if s[i] in check:
                stack.append(s[i])
            else:
                if stack:
                    if stack[-1] in check and check[stack[-1]]==s[i]:
                        stack.pop()
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
        return True if not stack else False
    

class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            '(':')', 
            '{':'}', 
            '[':']'
        }
        # s = "()[]{}"
        # 
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] in check:
                if check[stack[-1]] == c:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return True if not stack else False