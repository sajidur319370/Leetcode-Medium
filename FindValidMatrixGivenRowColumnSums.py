from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROW = len(rowSum)
        COl = len(colSum)
        res = [[0] * COl for _ in range(ROW)]
        for r in range(ROW):
            res[r][0] = rowSum[r]

        for c in range(COl - 1):
            curColSum = 0
            for r in range(ROW):
                curColSum += res[r][c]
            r = 0
            while curColSum > colSum[c]:
                diff = curColSum - colSum[c]
                max_shift = min(diff, res[r][c])
                res[r][c] -= max_shift
                res[r][c + 1] += max_shift
                curColSum -= max_shift
                r += 1

        return res


# Time:O(m * n)
# Space:O(m * n)

sn = Solution()
print(sn.restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))
print(sn.restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))
