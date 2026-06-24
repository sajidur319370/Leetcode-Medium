from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        cnt = defaultdict(int)
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            while cnt[nums[r]] > k:
                cnt[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


# Time:O(n)
# Space:O(n)


sn = Solution()
print(sn.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(sn.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(sn.maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
