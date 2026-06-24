import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        min_heap = [(0,0,0)] #(diff,r,c)
        visited = set()
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while min_heap:
            diff,r,c = heapq.heappop(min_heap)
            if (r,c) not in visited:
                visited.add((r,c))
                if r == rows-1 and c == cols-1:
                    return diff
                for dr,dc in direction:
                    nr = r+dr
                    nc = c+dc
                    if  0<= nr < rows and 0 <= nc < cols  and  (nr, nc) not in visited:
                        new_diff =max(diff,abs(heights[r][c]-heights[nr][nc]))
                        heapq.heappush(min_heap,(new_diff,nr,nc))
        return 0

# Time: O(m * n log(m * n))
# Space: O(m * n)

sn = Solution()
print(sn.minimumEffortPath( heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(sn.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]))
print(sn.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1]]))