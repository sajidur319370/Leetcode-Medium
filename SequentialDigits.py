from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        res = []
        q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

        while q:
            curr_num = q.popleft()
            if curr_num > high:
                continue

            if low <= curr_num <= high:
                res.append(curr_num)
            last_digit = curr_num % 10
            if last_digit < 9:
                next_num = (curr_num * 10) + (last_digit + 1)
                q.append(next_num)

        return res


# Time:O(1)
# Space:O(1)


sn = Solution()
print(sn.sequentialDigits(low=100, high=300))
print(sn.sequentialDigits(low=1000, high=13000))
