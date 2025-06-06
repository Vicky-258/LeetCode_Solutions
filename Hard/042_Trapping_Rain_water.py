from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]

        water = 0

        while left < right:

            if left_max < right_max:

                left += 1

                left_max = max(height[left], left_max)

                water += max(0, left_max - height[left])

            else:

                right -= 1

                right_max = max(height[right], right_max)

                water += max(0, right_max - height[right])

        return water
