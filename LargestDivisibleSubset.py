from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        res = []
        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    if len(temp) > len(dp[i]):
                        dp[i] = temp

            if len(dp[i]) > len(res):
                res = dp[i]
        return res


# Time:O(n^2)
# Space:O(n^2)


sn = Solution()
print(sn.largestDivisibleSubset([1, 2, 3]))
print(sn.largestDivisibleSubset([1, 2, 4, 8]))
print(sn.largestDivisibleSubset([1, 2, 3, 5, 15, 45]))
