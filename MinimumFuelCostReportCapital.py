from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj =  defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node ,parent):
            passenger = 0
            nonlocal  res
            for child in adj[node]:
              if child != parent:
                 p = dfs(child,node)
                 res += int(ceil(p/seats))
                 passenger += p

            return  passenger + 1
        res = 0
        dfs(0,-1)
        return res


# Time: O(n)
# Space: O(n)

sn = Solution()
print(sn.minimumFuelCost( roads = [[0,1],[0,2],[0,3]], seats = 5))
print(sn.minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))