from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] *= -1

        return res


sn = Solution()
print(sn.findDuplicates([3, 3, 3, 3, 3]))
print(sn.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
