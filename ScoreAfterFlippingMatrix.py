from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flip_cell(grid, r, c):
            if grid[r][c] == 1:
                grid[r][c] = 0
            else:
                grid[r][c] = 1

        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    flip_cell(grid, r, c)
        for c in range(cols):
            one_count = 0
            for r in range(rows):
                one_count += grid[r][c]
            if one_count < rows - one_count:
                for r in range(rows):
                    flip_cell(grid, r, c)
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += grid[r][c] << (cols - 1 - c)

        return res


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
