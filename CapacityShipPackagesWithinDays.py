from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r
        def hasCap(capacity):
            ships = 1
            remainCapacity = capacity
            for w in weights:
                if remainCapacity - w < 0:
                    ships += 1
                    remainCapacity = capacity
                remainCapacity -= w
            return ships <=days


        while l < r:
            m = l + ((r-l)//2)
            if hasCap(m):
                res = min(res, m)
                r = m-1
            else:
                l = m+1


        return res




sn = Solution()
print(sn.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(sn.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
print(sn.shipWithinDays(weights = [1,2,3,1,1], days = 4))