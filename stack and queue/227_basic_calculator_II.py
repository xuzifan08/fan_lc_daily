class Solution:
    def calculate(self, s: str) -> int:
        # "33 + 22 * 2"
        # stack = [33]
        n = len(s)
        if s == '0':
            return 0

        stack = []
        num = 0
        sign = '+'
        
        for i, v in enumerate(s):
            if v.isdigit():
                num = num * 10 + ord(v) - ord('0')
            if (not v.isdigit() and v != ' ') or i + 1 == n:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = v
                num = 0

        return sum(stack)