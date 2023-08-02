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
    


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(s) and ptr2 < len(t):
            while ptr2 < len(t) and s[ptr1]!=t[ptr2]:
                ptr2 += 1

            if ptr2 < len(t) and s[ptr1]== t[ptr2]:
                ptr1 += 1
                ptr2 += 1

        return True if ptr1 >= len(s) else False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        ptr_s = 0
        ptr_t = 0

        while ptr_s < len(s) and ptr_t < len(t):
            while ptr_t < len(t) and s[ptr_s]!= t[ptr_t]:
                ptr_t += 1

            if ptr_t < len(t) and s[ptr_s] == t[ptr_t]:
                ptr_s += 1
                ptr_t += 1

        return True if ptr_s >= len(s) else False