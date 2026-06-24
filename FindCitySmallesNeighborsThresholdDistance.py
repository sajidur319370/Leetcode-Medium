import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        def disktra(src):
            heap = [(0, src)]  # dist,node
            visited = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node not in visited:
                    visited.add(node)
                    for nei, nei_dist in adjList[node]:
                        new_dist = dist + nei_dist
                        if new_dist <= distanceThreshold:
                            heapq.heappush(heap, (new_dist, nei))

            return len(visited) - 1

        res = -1
        min_cnt = n
        for src in range(n):
            cnt = disktra(src)
            if cnt <= min_cnt:
                res = src
                min_cnt = cnt

        return res


# Time Complexity: O(n * m log m)
# Space Complexity: O(n + m)

sn = Solution()
print(sn.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
print(
    sn.findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2))
