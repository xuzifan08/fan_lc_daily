class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        output = []
        end = nums[0]
        start = nums[0]

        for num in nums[1:]:
            if end + 1 == num:
                end = num
            elif start == end:
                output.append(str(start))
                start = num
                end = num
            elif start < end:
                output.append(str(start)+"->" + str(end))
                start = num
                end = num
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start)+"->" + str(end))

        return output
