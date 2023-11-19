class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parentheses = 0
        close_parentheses = 0
 #     "(a(b(c)d)"  

        stack_parenthese = []
        stack_string = []

        for i, c in enumerate(s):
            if c != "(" and c!= ")":
                stack_string.append(c)
            elif c == "(":
                stack_string.append(c)
                stack_parenthese.append(c)
            elif c == ")":
                if stack_parenthese and stack_parenthese[-1] == "(":
                    stack_parenthese.pop()
                    stack_string.append(c)

        remove_open = len(stack_parenthese)
        
        if not remove_open: return "".join(stack_string)

        res = ""
        for string in reversed(stack_string):
            if remove_open and string == "(":
                remove_open-= 1
            else:
                res = string + res
        return res