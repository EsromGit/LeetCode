class Solution:
    def countDigits(self, num: int) -> int:
        counter = 0
        nums = num
        while nums > 0:
            digits = nums % 10
            if num % digits == 0:
                counter += 1
            nums //= 10
        return counter
