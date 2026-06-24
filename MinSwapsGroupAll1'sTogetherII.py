from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        tota_ones = 0
        for i in range(N):
            if nums[i] == 1:
                tota_ones += 1
        l = 0
        max_window_one = 0
        window_ones = 0
        for r in range(2 * N):
            if nums[r % N] == 1:
                window_ones += 1
            if r - l + 1 > tota_ones:
                window_ones -= nums[l % N]
                l += 1

            max_window_one = max(max_window_one, window_ones)

        return tota_ones - max_window_one


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]))
print(sn.minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]))
print(sn.minSwaps(nums=[1, 1, 0, 0, 1]))
