class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        temp, res = abs(x), 0

        while temp > 0:
            res = res * 10 + (temp % 10)
            temp //= 10

        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31

        if res < INT_MIN or res > INT_MAX:
            return 0
        else:
            return res * sign