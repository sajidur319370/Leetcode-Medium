import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst, cost in zip(original, changed, cost):
            adj[src].append((dst, cost))

        def disktra(src):
            heap = [(0, src)]
            min_dst_cost_map = {}
            while heap:
                cost, dst = heapq.heappop(heap)
                if dst not in min_dst_cost_map:
                    min_dst_cost_map[dst] = cost
                    for nei_dst, nei_cost in adj[dst]:
                        heapq.heappush(heap, (cost + nei_cost, nei_dst))
            return min_dst_cost_map

        min_cost_src_dst = {c: disktra(c) for c in set(source)}
        res = 0

        for src, dst in zip(source, target):
            if dst not in min_cost_src_dst[src]:
                return -1
            else:
                res += min_cost_src_dst[src][dst]

        return res


# Time:(26 * m + n)
# Space:O(m + n)

sn = Solution()
print(sn.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                     changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
