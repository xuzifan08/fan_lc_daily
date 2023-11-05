class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1

                longest = max(longest, length)
        return longest
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0


        for num in nums:
            if num - 1 not in nums_set:
                length = 1
                count = 1
                while num + count in nums_set:
                    length += 1
                    count += 1

                longest_seq = max(longest_seq, length)

        return longest_seq