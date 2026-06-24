from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        res = 0
        cnt = defaultdict(int)
        cnt[0] = 1

        for n in nums:
            prefix_sum += n
            remain = prefix_sum % k

            res += cnt[remain]
            cnt[remain] += 1

        return res

# Time:O(n)
# Space:O(k)

sn = Solution()
print(sn.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
print(sn.subarraysDivByK(nums = [5], k = 9))
