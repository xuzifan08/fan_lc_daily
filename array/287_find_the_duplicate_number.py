class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,4,2,2]
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)