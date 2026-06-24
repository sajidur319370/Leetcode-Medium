import heapq
from typing import List, Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        res = list(cnt.values())
        heapq.heapify(res)
        while k > 0:
            lowest = heapq.heappop(res)
            if lowest - k > 0:
                heapq.heappush(res, lowest - k)

            k -= lowest

        return len(res)


# Time: O(n log n)
# Space:O(n)

sn = Solution()
print(sn.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
