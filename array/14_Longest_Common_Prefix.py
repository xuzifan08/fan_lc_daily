class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i > len(string)-1 or string[i] != strs[0][i]:
                    return strs[0][:i]


        return strs[0]
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # strs = ["flower","flow","flight"]
        for i in range(len(strs[0])):
            for string in strs:
                if i + 1 > len(string) or strs[0][i]!= string[i]:
                    return strs[0][:i]

        return strs[0]
