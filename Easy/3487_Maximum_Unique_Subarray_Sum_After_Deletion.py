from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        mx = max(nums)
        if mx < 0:
            return mx

        seen = [False] * 201
        total = 0

        for num in nums:

            if num < 0:
                continue

            idx = num + 100
            if not seen[idx]:
                seen[idx] = True
                total += num

        return total