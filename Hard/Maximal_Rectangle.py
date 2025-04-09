from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        mini, width = 0, 0
        length = len(heights)

        for i in range(length):

            if stack:

                while stack and heights[stack[-1]] > heights[i]:
                    mini = stack.pop()

                    width = i if not stack else i - stack[-1] - 1

                    max_area = max(max_area, heights[mini] * width)

            stack.append(i)

        while stack:
            mini = stack.pop()
            width = length if not stack else length - stack[-1] - 1
            max_area = max(max_area, heights[mini] * width)

        return max_area
