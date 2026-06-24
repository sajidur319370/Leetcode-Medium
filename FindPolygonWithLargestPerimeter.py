from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        total = 0
        for n in nums:
            if total > n:
                ans = total + n
            total += n
        return ans


# Time:O(n)
# Space:O(1)


sn = Solution()
print(sn.largestPerimeter(nums=[5, 5, 5]))
print(sn.largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3]))
print(sn.largestPerimeter(nums=[5, 5, 50]))
