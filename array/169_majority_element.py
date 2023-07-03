class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map_ele = collections.defaultdict(int)

        for num in nums:
            map_ele[num] += 1

        maximum = nums[0]
        count = 1

        for ele, cnt in map_ele.items():
            if cnt > count:
                maximum = ele
                count = cnt

        return maximum