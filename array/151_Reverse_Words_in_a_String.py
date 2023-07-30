class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()

        left = 0
        right = len(s_list) - 1

        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        s_new = " ".join(s_list)

        return s_new