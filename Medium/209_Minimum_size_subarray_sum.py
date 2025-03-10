from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        min_len = float('inf')
        curr_sum = 0

        for right in range(len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(right - left + 1, min_len)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
