class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # "sadbutsad"
        #. 01234
        # "sad"
        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1