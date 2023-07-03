class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s = "abc", t = "ahbgdc"
        if len(s) > len(t):
            return False

        ptrs = 0
        ptrt = 0

        while ptrt < len(t) and ptrs < len(s):
            if s[ptrs] == t[ptrt]:
                ptrs += 1
            ptrt += 1

        if ptrs < len(s):
            return False
        return True
    