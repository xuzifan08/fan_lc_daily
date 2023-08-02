class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False

        seen = set()

        while n!= 1:
            n = self.sum_digits(n)

            if n not in seen:
                seen.add(n)
            else:
                return False
        return True

    def sum_digits(self, n:int):
        summation = 0
        while n > 0:
            remain = n % 10
            summation += remain * remain
            n //= 10

        return summation