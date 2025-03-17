from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        cnt = dict(Counter(nums))

        for key, value in cnt.items():

            if value % 2 != 0:
                return False

        return True