from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n
        for u, v in roads:
            edge_cnt[u] += 1
            edge_cnt[v] += 1

        res = 0
        label = 1
        for node in sorted(edge_cnt):
            res += node * label
            label += 1

        return res


# Time:O(n log n + E)
# Space:O(n)

sn = Solution()
print(sn.maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(sn.maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]))
