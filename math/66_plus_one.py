class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        carry = 0

        for i in range(len(digits)-1, -1, -1):
            summ = carry + digits[i]

            if summ > 9:
                digits[i] = summ % 10
                carry = summ // 10
            else:
                digits[i] = summ
                carry = 0

        if carry:
            digits = [carry] + digits

        return digits