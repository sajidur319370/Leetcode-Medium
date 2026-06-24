from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        r, c = rStart, cStart
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        steps = 1
        res = []
        while len(res) < rows * cols:
            for x in range(2):
                dr, dc = directions[i]
                for y in range(steps):
                    if (0 <= r < rows and 0 <= c < cols):
                        res.append([r, c])
                    r, c = r + dr, c + dc
                i = (i + 1) % 4
            steps += 1
        return res


# Time:O(m*n)
# Space:O(m*n)

sn = Solution()
print(sn.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4))
