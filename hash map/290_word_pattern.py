class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        def if_match(p, s):
            if len(p) != len(s): return False

            match = {}
            for i in range(len(p)):
                if p[i] not in match:
                    match[p[i]] = s[i]
                elif match[p[i]] != s[i]:
                    return False
            return True

        return if_match(pattern, s_list) and if_match(s_list, pattern)
