from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        y = total-x
        max_window = -1
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]

            while l <= r  and cur_sum > y:
                cur_sum -= nums[l]
                l+=1


            if cur_sum == y:
                max_window = max(max_window, r-l+1)

        return -1 if max_window == -1 else len(nums)- max_window

# Time Complexity	O(n)
# Space Complexity	O(1)

sn = Solution()
print(sn.minOperations(nums = [1,1,4,2,3], x = 5))
print(sn.minOperations(nums = [5,6,7,8,9], x = 4))
print(sn.minOperations(nums = [3,2,20,1,1,3], x = 10))