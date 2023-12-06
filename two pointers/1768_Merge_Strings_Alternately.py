class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = 1
        res = ""

        ptr_1 = 0
        ptr_2 = 0

        while ptr_1 < len(word1) and ptr_2 < len(word2):
            if first > 0:
                res += word1[ptr_1]
                ptr_1 += 1
            else:
                res += word2[ptr_2]
                ptr_2 += 1

            first = -1 * first

        if ptr_1 < len(word1):
            res += word1[ptr_1:]

        if ptr_2 < len(word2):
            res += word2[ptr_2:]

        return res
    


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1 = 0
        ptr_2 = 0
        alternate = 1
        res = ""

        while ptr_1 < len(word1) and ptr_2 < len(word2):
            if alternate > 0:
                res += word1[ptr_1]
                ptr_1 += 1
                
            elif alternate < 0:
                res += word2[ptr_2]
                ptr_2 += 1
            alternate = -alternate

        if ptr_1 < len(word1):
            res += word1[ptr_1:]
        
        if ptr_2 < len(word2):
            res += word2[ptr_2:]

        return res
