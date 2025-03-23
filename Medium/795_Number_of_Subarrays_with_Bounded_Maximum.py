from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        last_valid = -1
        last_invalid = -1
        count = 0

        for i, num in enumerate(nums):
            if num > right:
                last_invalid = i
            if left <= num <= right:
                last_valid = i

            count += max(0, last_valid - last_invalid)

        return count
