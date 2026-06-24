from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        sumArray = []
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                sumArray.append(sum)
        sumArray.sort()
        res = 0
        for i in range(left - 1, right):
            res += sumArray[i]
        return res % MOD


# Time:O(n^2 log n )
# Space:O(n^2)

sn = Solution()
print(sn.rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))
