class Solution:
    def candy(self, ratings: List[int]) -> int:
        # [1,0,2]
        #.[1 1 1]
        # [2,]
        candy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and candy[i]<= candy[i-1]:
                candy[i] = candy[i-1] + 1
                # print(i, candy)

        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j + 1] and candy[j] <= candy[j+1]:
                candy[j] = candy[j+1] + 1
                # print(i, candy)

        return sum(candy)