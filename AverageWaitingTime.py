from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        time = 0
        totalWaitingTime = 0
        for arrival, waiting in customers:
            if time > arrival:
                totalWaitingTime += (time - arrival)
            else:
                time = arrival
            totalWaitingTime += waiting
            time += waiting

        return totalWaitingTime / len(customers)


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))
print(sn.averageWaitingTime(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))
