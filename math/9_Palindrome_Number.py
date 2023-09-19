class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        
        while x >= div * 10:
            div *= 10

        while x:
            left = x // div
            right = x % 10

            if left != right:
                return False
            print(x // 10)
            x = (x % div) // 10

            div = div / 100

        return True