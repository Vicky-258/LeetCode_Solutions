from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        flag_col = False
        flag_row = False

        for i in range(m):
            if matrix[i][0] == 0:
                flag_col = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                flag_row = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for col in range(1, n):
            if matrix[0][col] == 0:
                for i in range(1, m):
                    matrix[i][col] = 0

        for row in range(1, m):
            if matrix[row][0] == 0:
                for j in range(1, n):
                    matrix[row][j] = 0

        if flag_col:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row:
            for j in range(n):
                matrix[0][j] = 0
