from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)

        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  # current player's score

            for j in range(i):
                # No conflict condition
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)

# Time: O(n^2)
# Space: O(n)

sn = Solution()
print(sn.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(sn.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))