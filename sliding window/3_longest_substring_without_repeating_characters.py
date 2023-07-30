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
    


    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        # "pwwkew"
        counter = collections.defaultdict(int)
        max_len = 0
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1

            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
    
    # for every iteration, check if this val appears more than once, if so, keep shrinking left side until it decreases to 



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
        # "pwwkew"

        left = 0
        seen = collections.defaultdict(int)
        length = 0

        for right in range(len(s)):
            seen[s[right]] += 1

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)

        return length
