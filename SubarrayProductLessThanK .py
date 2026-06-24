from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        prod = 1
        l = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1
            res += (r - l + 1)

        return res


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(sn.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
