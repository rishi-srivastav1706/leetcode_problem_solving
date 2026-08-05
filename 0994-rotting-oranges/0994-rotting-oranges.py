from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0
        time = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        if not queue:
            return -1

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            size = len(queue)

            while size > 0:
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if (0 <= newRow < m and
                        0 <= newCol < n and
                        grid[newRow][newCol] == 1):

                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1

                size -= 1

            time += 1

        return time if fresh == 0 else -1