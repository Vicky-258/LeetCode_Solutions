from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        num_zero = 0
        max_len = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                num_zero += 1

            while num_zero > 1:
                if nums[left] == 0:
                    num_zero -= 1
                left += 1

            max_len = max(right - left + 1, max_len)

        return max_len - 1