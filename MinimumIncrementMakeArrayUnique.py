from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                res += 1+nums[i-1]-nums[i]
            nums[i] = nums[i-1]+1
        return res

# Time:O(N)
# Space:O(1)

sn = Solution()
print(sn.minIncrementForUnique(nums = [1,2,2]))
print(sn.minIncrementForUnique(nums = [3,2,1,2,1,7]))