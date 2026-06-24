from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float('inf')
        for l in range(4):
            r = len(nums) - 4 + l
            res = min(res, nums[r] - nums[l])
        return res


# Time:O(n log n)
# Space:O(1)

sn = Solution()
print(sn.minDifference(nums=[5, 3, 2, 4]))
print(sn.minDifference(nums=[1, 5, 0, 10, 14]))
print(sn.minDifference(nums=[3, 100, 20]))
