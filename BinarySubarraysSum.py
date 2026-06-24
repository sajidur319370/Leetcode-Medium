from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count subarray to make a sum equal or less than x
        def count_subarr(x):
            if x < 0:
                return 0
            res = 0
            l = 0
            cur_sum = 0
            for r in range(len(nums)):
                cur_sum += nums[r]
                while cur_sum > x:
                    cur_sum -= nums[l]
                    l += 1
                res += (r - l + 1)

            return res

        return count_subarr(goal) - count_subarr(goal - 1)


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(sn.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
