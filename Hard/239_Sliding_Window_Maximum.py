from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        res = []

        for right in range(len(nums)):

            if q and q[0] < right - k + 1:
                q.popleft()

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if right >= k - 1:
                res.append(nums[q[0]])

        return res
