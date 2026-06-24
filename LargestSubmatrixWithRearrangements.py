from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        res = 0
        prev_height = [0] * col
        for i in range(row):
            height = matrix[i][:]
            for j in range(col):
                if height[j] > 0:
                    height[j] += prev_height[j]
            sorted_height = sorted(height, reverse=True)
            for k in range(col):
                res = max(res, (k + 1) * sorted_height[k])

            prev_height = height[:]

        return res


# Time:O(m * n)
# Space:O(m * n)

sn = Solution()
print(sn.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(sn.largestSubmatrix([[1, 0, 1, 0, 1]]))
print(sn.largestSubmatrix([[1, 1, 0], [1, 0, 1]]))
