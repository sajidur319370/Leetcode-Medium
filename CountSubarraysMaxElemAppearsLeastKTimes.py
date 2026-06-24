from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_cnt = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == max_num:
                max_cnt += 1
            while max_cnt == k:
                if nums[l] == max_num:
                    max_cnt -= 1
                l += 1
            res += l

        return res


# Time Complexity: O(n)
# Space Complexity:O(1)


sn = Solution()
print(sn.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print(sn.countSubarrays(nums=[1, 4, 2, 1], k=3))
