from math import ceil
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumWeight = sum(stones)
        target= ceil(sumWeight / 2)
        cache = {}
        def dfs(i,total):
            if total >= target or i==len(stones):
                return abs(sumWeight - 2 * total)
            if (i, total) in cache:
                return cache[(i, total)]
            cache[(i,total)]  = min(dfs(i+1,total),dfs(i+1,total+stones[i]))
            return cache[(i, total)]
        return dfs(0,0)


# Time Complexity: O(N * S)
# Space Complexity: O(N * S)


sn = Solution()
print(sn.lastStoneWeightII(stones = [2,7,4,1,8,1]))
print(sn.lastStoneWeightII(stones = [31,26,33,21,40]))