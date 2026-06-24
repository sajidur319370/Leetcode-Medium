from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        res = []
        for i, n in enumerate(nums):
            left_len = i
            right_len = len(nums) - i - 1
            right_sum = total_sum - (n + left_sum)
            diff_sum = (left_len * n) - left_sum + right_sum - (n * right_len)
            res.append(diff_sum)
            left_sum += n

        return res


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.getSumAbsoluteDifferences(nums=[2, 3, 5]))
print(sn.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))
