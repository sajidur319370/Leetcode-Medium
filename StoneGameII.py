from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp ={}
        def dfs(alice,i,M):
            if i == len(piles):
                return 0
            if (alice,i,M) in dp:
                return dp[(alice,i,M)]
            res = 0 if alice else float('inf')
            total = 0
            for X in range (1,2 * M + 1):
                if i+X <= len(piles):
                    total += piles[X+i-1]
                    if alice:
                        res = max(res, total + dfs(not alice,i+X,max(M,X)))
                    else:
                        res = min(res, dfs(not alice,i+X,max(M,X)))
            dp[(alice,i,M)] = res
            return dp[(alice,i,M)]
        return dfs(True,0,1)


# Time:O(n^3)
# Space:O(n^2)
        




sn =  Solution()
print(sn.stoneGameII(piles = [2,7,9,4,4]))
print(sn.stoneGameII(piles = [1,2,3,4,5,100]))