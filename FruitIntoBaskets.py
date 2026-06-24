from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt  =  defaultdict(int)
        l = 0
        total = 0
        res = 0
        for r in range(len(fruits)):
            cnt[fruits[r]] += 1
            total += 1

            while len(cnt)>2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del cnt[fruits[l]]
                total -=   1
                l+=1
            res = max(res, total)

        return res


# Time: O(n)
# Space: O(1)

sn = Solution()
print(sn.totalFruit([1,2,1]))
print(sn.totalFruit([0,1,2,2]))
print(sn.totalFruit([1,2,3,2,2]))