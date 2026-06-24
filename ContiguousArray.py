from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one = 0
        zero = 0
        diff_idx = {}
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_idx:
                diff_idx[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_idx[one - zero]
                res = max(res, i - idx)

        return res


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.findMaxLength(nums=[0, 1, 0]))
print(sn.findMaxLength(nums=[0, 1, 1, 1, 1, 1, 0, 0, 0]))
