from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels = set(jewels)

        cnt = 0

        for ch in stones:

            if ch in jewels:
                cnt += 1

        return cnt
