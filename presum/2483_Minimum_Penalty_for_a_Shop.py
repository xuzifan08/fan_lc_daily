class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # "YYNY"
        #. 
        pre_n = [0]*(len(customers) + 1)
        post_y = [0]*(len(customers) + 1)

        for i in range(1, len(pre_n)):
            if customers[i-1] == "N":
                pre_n[i] = pre_n[i-1] + 1
            else:
                pre_n[i] = pre_n[i-1]

        for j in range(len(post_y)-2, -1,-1):
            if customers[j] == "Y":
                post_y[j] = post_y[j+1] + 1
            else:
                post_y[j] = post_y[j+1]

        cur_sum = pre_n[0] + post_y[0]
        cur_idx = 0
        for idx in range(1,len(pre_n)):
            if pre_n[idx] + post_y[idx] < cur_sum:
                cur_sum = pre_n[idx] + post_y[idx]
                cur_idx = idx

        return cur_idx