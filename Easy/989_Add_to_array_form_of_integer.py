from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        i = len(num) - 1

        carry = k

        while i >= 0 and carry > 0:
            x = num[i] + carry

            carry, num[i] = divmod(x, 10)

            i -= 1

        while carry > 0:
            carry, digit = divmod(carry, 10)
            num.insert(0, digit)

        return num