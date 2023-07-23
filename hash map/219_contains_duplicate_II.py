class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}

        for i, v in enumerate(nums):
            if v in checked and i - checked[v]<=k:
                return True

            checked[v] = i

        return False
