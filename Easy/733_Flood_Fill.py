from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        queue = deque()
        queue.append((sr, sc))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:

            row, col = queue.popleft()
            image[row][col] = color

            for dx, dy in directions:

                nx, ny = row + dx, col + dy

                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == start_color:

                    queue.append((nx, ny))

        return image