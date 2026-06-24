from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res


# Time:O(n)
# Sapce:O(1)

sn = Solution()
print(sn.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(sn.minCost(colors="abc", neededTime=[1, 2, 3]))
print(sn.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
