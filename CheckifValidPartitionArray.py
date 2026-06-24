from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)

        dp[0] = True  # empty array is valid

        for i in range(2, n + 1):

            # Case 1: Two equal elements
            if nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True

            # Case 2 & 3: Three elements
            if i >= 3:
                # Case 2: Three equal elements
                if (nums[i - 1] == nums[i - 2] == nums[i - 3]) and dp[i - 3]:
                    dp[i] = True

                # Case 3: Consecutive increasing elements
                if (nums[i - 3] + 1 == nums[i - 2] and
                        nums[i - 2] + 1 == nums[i - 1] and
                        dp[i - 3]):
                    dp[i] = True

        return dp[n]




#Time: O(n)
#Space: O(n)
sn=  Solution()
print(sn.validPartition(nums = [4,4,4,5,6]))
print(sn.validPartition(nums = [1,1,1,2]))