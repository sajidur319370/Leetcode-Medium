from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for num in arr:
            prev = (prev + 1, num)
        return prev


# Time:O(n)
# Space:O(1)
sn = Solution()
print(sn.maximumElementAfterDecrementingAndRearranging(arr=[2, 2, 1, 2, 1]))
print(sn.maximumElementAfterDecrementingAndRearranging(arr=[100, 1, 1000]))
print(sn.maximumElementAfterDecrementingAndRearranging(arr=[1, 2, 3, 4, 5]))
