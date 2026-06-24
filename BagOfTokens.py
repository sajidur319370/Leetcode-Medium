from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        score = 0
        l = 0
        r = len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
            res = max(res, score)
        return res


# Time:O(n log n)
# Space: O(1)

sn = Solution()
print(sn.bagOfTokensScore(tokens=[100], power=50))
print(sn.bagOfTokensScore(tokens=[200, 100], power=150))
print(sn.bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
