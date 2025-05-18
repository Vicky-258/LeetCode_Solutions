from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int] | None:

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i

        return None