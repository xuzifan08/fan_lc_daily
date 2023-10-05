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
    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)

        for num in nums:
            counter[num] += 1

        val_so_far = nums[0]
        max_count = 0
        for val, count in counter.items():
            if count > max_count:
                max_count = count
                val_so_far = val

        return val_so_far