from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float | None:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (total_len + 1) // 2 - i

            L1 = float('-inf') if i == 0 else nums1[i - 1]
            R1 = float('inf') if i == m else nums1[i]
            L2 = float('-inf') if j == 0 else nums2[j - 1]
            R2 = float('inf') if j == n else nums2[j]

            if L1 <= R2 and L2 <= R1:
                if total_len % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                else:
                    return max(L1, L2)
            elif L1 > R2:
                high = i - 1
            else:
                low = i + 1
        return None