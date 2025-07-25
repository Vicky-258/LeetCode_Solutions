from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []
        if not nums:
            return res
        left = 0

        for right in range(1, len(nums)):

            if nums[right] != nums[right - 1] + 1:
                if left == right - 1:
                    res.append(str(nums[left]))
                else:
                    res.append(f"{nums[left]}->{nums[right - 1]}")
                left = right

        if left == len(nums) - 1:
            res.append(f"{nums[-1]}")
        else:
            res.append(f"{nums[left]}->{nums[len(nums)-1]}")

        return res