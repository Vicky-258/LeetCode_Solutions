from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        curr = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
            print(nums)
