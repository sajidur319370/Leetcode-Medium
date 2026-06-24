from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()  # incr
        max_q = deque()  # dcr
        res = 0
        l = 0
        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])

            while min_q and max_q and max_q[0] - min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft()
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1
            res = max(res, r - l + 1)

        return res


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.longestSubarray(nums=[8, 2, 4, 7], limit=4))
print(sn.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
print(sn.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
