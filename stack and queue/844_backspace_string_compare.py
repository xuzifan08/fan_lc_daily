class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:  
        def type(s):
            stack = []

            for c in s:
                if stack and c == '#':
                    stack.pop()
                elif c == '#':
                    continue
                else:
                    stack.append(c)

            return "".join(stack)

        return type(s) == type(t)