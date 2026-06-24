from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        def isValid(threshold) -> bool:
            i = 0
            cnt = 0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= threshold:
                    i+=2
                    cnt += 1
                else:
                    i+=1
                if cnt == p:
                    return True
            return False
        nums.sort()
        left = 0
        right = 10**9
        result = 10**9

        while left <= right:
            mid = left + (right-left)//2
            if isValid(mid):
                right = mid-1
                result = mid
            else:
                left = mid+1

        return result


# Time:O(N log M)
# Space:O(1)

sn = Solution()
print(sn.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
print(sn.minimizeMax(nums = [4,2,1,2], p = 1))