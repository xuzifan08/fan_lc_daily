class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrance = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and last_occurrance[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)

        return "".join(stack)
    

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurance = {c:i for i, c in enumerate(s)}

        stack = []
        seen = set()

        for idx, val in enumerate(s):
            if val not in seen:
                while stack and val < stack[-1] and last_occurance[stack[-1]] > idx:
                    v = stack.pop()
                    seen.remove(v)
                stack.append(val)
                seen.add(val)

        return "".join(stack)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # "cbacdcbc"
        #  01234
        # last_occurance = {b:3,c:4,a:2}
        #  stack = [a,b]
        #  seen = {a,b}
        last_occurance = {c:i for i, c in enumerate(s)}
        
        stack = []
        seen = set()

        for idx, val in enumerate(s):
            if val not in seen:
                while stack and val < stack[-1] and last_occurance[stack[-1]] > idx:
                    v = stack.pop()
                    seen.remove(v)
                stack.append(val)
                seen.add(val)
        return "".join(stack)