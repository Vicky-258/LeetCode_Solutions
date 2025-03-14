from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1_case1, prev2_case1 = 0, nums[0]
        prev1_case2, prev2_case2 = 0, nums[1]

        for i in range(1, len(nums) - 1):
            prev1_case1, prev2_case1 = prev2_case1, max(prev2_case1, prev1_case1 + nums[i])
            prev1_case2, prev2_case2 = prev2_case2, max(prev2_case2, prev1_case2 + nums[i + 1])

        return max(prev2_case1, prev2_case2)
