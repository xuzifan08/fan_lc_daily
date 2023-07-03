class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        str_count = collections.defaultdict(int)
        max_str = 0


        for r in range(len(s)):
            str_count[s[r]] += 1
            while str_count[s[r]] > 1:
                 str_count[s[l]] -= 1
                 l += 1
            max_str = max(max_str, r - l + 1)

        return max_str