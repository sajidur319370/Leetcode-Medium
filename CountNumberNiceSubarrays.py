from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        l = 0
        m = 0
        res = 0
        odd = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l
            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m - l + 1)
        return res


# Time:O(n)
# Space:O(1)


sn = Solution()
print(sn.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(sn.numberOfSubarrays(nums=[2, 4, 6], k=1))
print(sn.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
