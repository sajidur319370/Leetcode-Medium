class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7
        grid = [[0] * n for _ in range(m)]

        for _ in range(1, maxMove + 1):
            temp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if r + 1 == m:
                        temp[r][c] = (temp[r][c] + 1) % mod
                    else:
                        temp[r][c] = (temp[r][c] + grid[r + 1][c]) % mod
                    if r - 1 < 0:
                        temp[r][c] = (temp[r][c] + 1) % mod
                    else:
                        temp[r][c] = (temp[r][c] + grid[r - 1][c]) % mod
                    if c + 1 == n:
                        temp[r][c] = (temp[r][c] + 1) % mod
                    else:
                        temp[r][c] = (temp[r][c] + grid[r][c + 1]) % mod

                    if c - 1 < 0:
                        temp[r][c] = (temp[r][c] + 1) % mod
                    else:
                        temp[r][c] = (temp[r][c] + grid[r][c - 1]) % mod

            grid = temp

        return grid[startRow][startColumn]


# Time:O(m* n * move)
# Space:O(m * n)


sn = Solution()
print(sn.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(sn.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
