from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window = 0
        max_window_satisfied = 0
        satisfied = 0
        for r in range(len(customers)):
            if grumpy[r] == 1:
                window += customers[r]
            else:
                satisfied += customers[r]

            if r-l+1>minutes:
                if grumpy[l] == 1:
                    window -= customers[l]
                l+=1
            max_window_satisfied = max(max_window_satisfied, window)
        return satisfied+ max_window_satisfied


# Time:O(n)
# Space:O(1)


sn = Solution()
print(sn.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
print(sn.maxSatisfied(customers = [1], grumpy = [0], minutes = 1))

