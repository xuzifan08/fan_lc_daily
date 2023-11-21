class Solution:
    def validPalindrome(self, s: str) -> bool:
        # "baccabe"
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left]!= s[right]:
                string1 = s[left+1:right+1]
                string2 = s[left:right]
                return string1 == string1[::-1] or string2 == string2[::-1]
            left += 1
            right -= 1

        return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # "baccabe"
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left]!=s[right]:
                string1 = s[left:right]
                string2 = s[left+1:right+1]
                return string1==string1[::-1] or string2==string2[::-1]

            left += 1
            right -= 1

        return True
