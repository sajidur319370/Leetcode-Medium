from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        q = deque(range(len(deck)))
        for n in deck:
            i = q.popleft()
            res[i] = n
            if q:
                q.append(q.popleft())

        return res


# Time:O(N log N)
# Space:O(N)

sn = Solution()
print(sn.deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]))
