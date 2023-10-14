class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}


        def lps(l, r):
            if l > r:
                return 0
            if l == r:
                return 1

            if (l, r) in dp:
                return dp[(l, r)]

            if s[l] == s[r]:
                dp[(l, r)] =  lps(l + 1, r - 1) + 2

            else:
                dp[(l, r)] = max(lps(l+1, r), lps(l, r-1))
            return dp[(l, r)] 
            


        return lps(0, len(s)-1)#longest palindromic subsequence