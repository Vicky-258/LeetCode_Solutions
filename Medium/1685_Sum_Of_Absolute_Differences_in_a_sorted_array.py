from typing import List
import itertools

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []

        n = len(nums)

        prefix = list(itertools.accumulate(nums))

        total = prefix[-1]

        for i in range(n):
            left = i * nums[i] - prefix[i - 1] if i > 0 else 0

            right = (total - prefix[i]) - (n - i - 1) * nums[i]

            res.append(left + right)

        return res