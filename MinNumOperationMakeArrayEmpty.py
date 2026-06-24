from math import ceil
from typing import List, Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_arr = Counter(nums)
        res = 0
        for num, cnt in count_arr.items():
            if cnt == 1:
                return -1
            res += ceil(cnt / 3)

        return res


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(sn.minOperations([2, 1, 2, 2, 3, 3]))
