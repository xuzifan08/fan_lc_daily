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
