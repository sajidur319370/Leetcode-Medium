import heapq
from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def inbounds(i, j):
            return 0 <= i < N and 0 <= j < N

        def precompute():
            q = deque()
            min_dist = {}
            for i in range(N):
                for j in range(N):
                    if grid[i][j]:
                        q.append((i, j, 0))
                        min_dist[(i, j)] = 0
            while q:
                i, j, dist = q.popleft()
                neighbors = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                for ni, nj in neighbors:
                    if inbounds(ni, nj) and (ni, nj) not in min_dist:
                        q.append((ni, nj, dist + 1))
                        min_dist[(ni, nj)] = dist + 1
            return min_dist

        min_dist = precompute()
        max_heap = [(-min_dist[(0, 0)], 0, 0)]
        visit = set()
        visit.add((0, 0))
        while max_heap:
            dist, i, j = heapq.heappop(max_heap)
            dist = -dist
            if i == N - 1 and j == N - 1:
                return dist
            neighbors = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            for ni, nj in neighbors:
                if inbounds(ni, nj) and (ni, nj) not in visit:
                    visit.add((ni, nj))
                    dist2 = min(dist, min_dist[(ni, nj)])
                    heapq.heappush(max_heap, (-dist2, ni, nj))


# Time:O(n^2 log N)
# Space:O(N^2)


sn = Solution()
print(sn.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(sn.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
