class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = []
        pre_sum = 0
        for num in w:
            pre_sum += num
            self.pre_sum.append(pre_sum)
        self.total_sum = pre_sum
            
    def pickIndex(self) -> int:
        index = self.total_sum * random.random()
        low = 0
        high = len(self.pre_sum)-1

        while low < high:
            mid = low + (high - low) // 2
            if index > self.pre_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low