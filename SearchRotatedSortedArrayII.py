from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            #Duplicate case
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            #Left side sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            #Right side sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# Average: O(log n)
# Worst:   O(n)
# Space:   O(1)

sn = Solution()
print(sn.search(nums = [2,5,6,0,0,1,2], target = 0))
print(sn.search(nums = [2,5,6,0,0,1,2], target = 3))