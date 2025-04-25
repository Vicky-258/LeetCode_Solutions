from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int|float:

        m, n = len(grid), len(grid[0])

        dp = [float('inf')] * n
        dp[0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

        return dp[-1]