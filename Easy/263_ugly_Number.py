class Solution:
    def isUgly(self, n: int) -> bool:

        if n < 1:
            return False

        order = [2, 3, 5]

        count = 0
        for p in order:
            while n % p == 0:
                n //= p
                count += 1

        return n == 1
