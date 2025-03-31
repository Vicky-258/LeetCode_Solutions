from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        low, high = 0, min(len(word) for word in strs)

        while low < high:

            mid = (low + high + 1) // 2

            prefix = strs[0][:mid]
            flag = all(word.startswith(prefix) for word in strs)

            if flag:

                low = mid

            else:
                high = mid - 1

        return strs[0][:low]