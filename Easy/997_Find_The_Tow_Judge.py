from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        degrees = {i: [0, 0] for i in range(1, n + 1)}

        for i, j in trust:
            degrees[i][1] += 1
            degrees[j][0] += 1

        for key, value in degrees.items():

            if value[0] == n - 1 and value[1] == 0:
                return key

        return -1
