from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        curr = 0

        for i in range(len(nums) - 1):

            if nums[i] != nums[curr]:
                nums[curr] = nums[i]
                curr = i

            if nums[i] == nums[i + 1]:
                curr = i + 1

        return curr