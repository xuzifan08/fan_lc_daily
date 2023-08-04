class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))

            else:
                right = stack.pop()
                left = stack.pop()
                if i == '+':
                    stack.append(left+right)
                elif i == '-':
                    stack.append(left - right)
                elif i == '*':
                    stack.append(left * right)
                else:
                    if left * right < 0 and left%right !=0:
                        stack.append(left // right + 1)
                    else:
                        stack.append(left // right)

        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(token)

            else:
                res = 0
                right = int(stack.pop())
                left = int(stack.pop())
                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                elif token == '/':
                    if left * right < 0 and left % right !=0:
                        res=left // right + 1
                    else:
                        res=left // right
                stack.append(res)
        return int(stack[0])