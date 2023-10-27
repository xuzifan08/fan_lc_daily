class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the point is to figure out the constrains
        stack = []
        res = []


        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))

            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return res
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # the point is to figure out the constrains
        res = []
        stack = []

        def backtrack(stack, open, close):
            if open == close == n:
                res.append("".join(stack))
            
            if open < n:
                stack.append("(")
                backtrack(stack, open + 1, close)
                stack.pop()

            if open > close:
                stack.append(")")
                backtrack(stack, open, close + 1)
                stack.pop()

        backtrack(stack, 0,0)

        return 
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open, close, stack):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open+1,close,stack)
                stack.pop()

            if open > close:
                stack.append(")")
                backtrack(open,close+1,stack)
                stack.pop()

        backtrack(0,0,[])


        return res
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # ["((()))","(()())","(())()","()(())","()()()"]
        def backtrack(curr, open, close):
            if open == close == n:
                res.append("".join(curr))
                return

            if open < n:
                curr.append("(")
                backtrack(curr, open + 1, close)
                curr.pop()

            if open > close:
                curr.append(")")
                backtrack(curr, open, close + 1)
                curr.pop()

        backtrack([],0,0)
        return res