from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1

        curr_area, max_area = 0, -1

        while i <= j:

            curr_area = (j - i) * min(height[i], height[j])
            max_area = max(curr_area, max_area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area