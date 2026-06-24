from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:

        res = 0
        for m in range(1, len(rating) - 1):
            left_smaller_cnt = 0
            right_larger_cnt = 0
            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller_cnt += 1
            for i in range(m + 1, len(rating)):
                if rating[i] > rating[m]:
                    right_larger_cnt += 1

            res += left_smaller_cnt * right_larger_cnt
            left_larger_cnt = m - left_smaller_cnt
            right_smaller_cnt = len(rating) - (m + 1) - right_larger_cnt
            res += left_larger_cnt * right_smaller_cnt

        return res


# Time:O(n^2)
# Space:O(1)

sn = Solution()
print(sn.numTeams(rating=[2, 5, 3, 4, 1]))
print(sn.numTeams(rating=[2, 1, 3]))
print(sn.numTeams(rating=[1, 2, 3, 4]))
