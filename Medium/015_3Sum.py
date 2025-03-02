from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        # 4. If there are at least 3 zeros in the list, include (0, 0, 0)
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 5. For all pairs of negative numbers, check if their complement exists in positives
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 6. For all pairs of positive numbers, check if their complement exists in negatives
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        # Convert set to list of lists
        return [list(triplet) for triplet in res]
