from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -float('inf')

        current_sum = 0

        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])

            maxi = max(maxi, current_sum)

        return maxi
