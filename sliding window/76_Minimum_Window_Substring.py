class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t== "":
            return ""

        left = 0
        t_count = collections.Counter(t)
        window = collections.defaultdict(int)

        res = [-1, -1]
        res_len = float('inf')

        have = 0
        need = len(t_count)

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in t_count and t_count[char] == window[char]:
                have += 1
            
            while have == need:
                if right - left +1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -=1
                left += 1

                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1
        l, r = res

        return s[l: r+1] if res_len != float('inf') else ""
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not len(t): return ""

        t_count = collections.Counter(t)
        t_found = collections.defaultdict(int)
        left = 0
        length = float('inf')
        need = len(t_count)
        have = 0

        res = [-1, -1]


        for right in range(len(s)):
            char = s[right]
            t_found[char] += 1

            if char in t_count and t_count[char] == t_found[char]:
                have += 1

            while have == need:
                if right - left + 1 < length:
                    res = [left, right]
                    length =  right - left + 1

                left_char= s[left]
                t_found[left_char] -=1
                left += 1

                if left_char in t_count and t_found[left_char] <t_count[left_char]:
                    have -= 1

        r, l = res
        
        return s[r:l+1] if length != float('inf') else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "": 
            return ""
        left = 0
        t_count = collections.Counter(t)
        t_found = collections.defaultdict(int)

        res = [-1, -1]
        length = float('inf')
        need = len(t_count)
        have = 0

        for right in range(len(s)):
            char = s[right]
            t_found[char] += 1

            if char in t_count and t_found[char] == t_count[char]:
                have += 1

            while have == need:
                if right -left + 1 < length:
                    res = [left, right]
                    length = right - left + 1
                    print(res)
                    print(s)

                left_char = s[left]
                t_found[left_char] -= 1
                left += 1

                if left_char in t_count and t_found[left_char]< t_count[left_char]:
                    have -= 1

        l, r = res

        return s[l:r+1] if length != float('inf') else ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # found all the diff char
        # and num of char found too

        min_size = len(s) + 1
        t_count = collections.Counter(t)
        t_found = collections.defaultdict(int)
        need = len(t_count)
        have = 0
        left = 0
        res = [-1,-1]

        for right in range(len(s)):
            t_found[s[right]] += 1
            
            if s[right] in t_count and t_count[s[right]] == t_found[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < min_size:
                    min_size = right - left + 1
                    res = [left, right]

                t_found[s[left]] -= 1
                if s[left] in t_count and t_found[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        left, right = res

        return s[left:right+ 1] if min_size!= len(s)+1 else ""
    


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # found all the diff char
        # and num of char found too
        t_count = collections.Counter(t)
        need = len(t_count)
        have = 0
        s_found = collections.defaultdict(int)
        left = 0
        res = [-1,-1]
        min_size = len(s) + 1

        for right in range(len(s)):
            s_found[s[right]] += 1
            if s[right] in t_count and t_count[s[right]] == s_found[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < min_size:
                    res = [left, right]
                    min_size = right - left + 1

                s_found[s[left]] -= 1
                if s[left] in t_count and s_found[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
                
        l, r = res

        return s[l:r + 1]