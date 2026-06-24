from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def outbounds(r, c):
            return r < 0 or c < 0 or r >= rows or c >= cols

        def visited_cells(r, c, visited):
            return (r, c) in visited

        def empty_grid(r, c, grid):
            return grid[r][c] == 0

        def dfs(r, c, visited):
            if (outbounds(r, c)
                    or empty_grid(r, c, grid)
                    or visited_cells(r, c, visited)):
                return 0

            visited.add((r, c))
            res = grid[r][c]
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbors:
                res = max(res, grid[r][c] + dfs(nr, nc, visited))
            visited.remove((r, c))
            return res

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, set()))
        return res


# Time complexity: O(N * 3^N)
# Space complexity: O(N)

sn = Solution()
print(sn.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]
                        ))
print(sn.getMaximumGold(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
