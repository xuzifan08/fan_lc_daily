class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            if target - v not in seen:
                seen[v] = i
            else:
                return [i, seen[target - v]]

        return -1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            if target - v in seen:
                return [seen[target - v], i]

            else:
                seen[v] = i