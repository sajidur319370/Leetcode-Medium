import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []

        for i in range(len(heights) - 1):
            diff_height = heights[i + 1] - heights[i]

            if diff_height > 0:
                bricks -= diff_height
                heapq.heappush(max_heap, -diff_height)

                if bricks < 0:
                    if ladders == 0:
                        return i
                    ladders -= 1
                    bricks += -heapq.heappop(max_heap)

        return len(heights) - 1


# Time:O(n log n)
# Space:O(n)

sn = Solution()
print(sn.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(sn.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
