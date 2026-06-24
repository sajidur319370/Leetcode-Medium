from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i - 1][0])
        return res


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))
print(sn.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
