from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        ans = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                ans[i] = nums[k]
                i += 2
            else:
                ans[j] = nums[k]
                j += 2
        return ans


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.rearrangeArray([3, 1, -2, -5, 2, -4]))
print(sn.rearrangeArray([-1, 1]))
print(sn.rearrangeArray([1, -2, -3, 4]))
