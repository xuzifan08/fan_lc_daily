class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]* (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]* (len(s)+1)
        dp[0] = True

        # "leetcode"
        #. 012i4567

        for i in range(len(s)):
            for w in wordDict:
                print(i)
                print(len(w))
                print(s[i+1-len(w):i+1])
                print(i-len(w))
                print("------")
                if i+1 >= len(w) and s[i+1-len(w):i+1]== w:
                    dp[i+1] = dp[i+1-len(w)]
                if dp[i+1]:
                    break

        return dp[len(s)]
    

## that's why we want to start from the end, it's easier for indexing


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        # "leetcode"
        #  01234567
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: # this conition is important to prevent setting dp[i] to False again
                    break


        return dp[0]
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True
        # "leetcode"

        #. 01234567
        #      4 +4  

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
                    