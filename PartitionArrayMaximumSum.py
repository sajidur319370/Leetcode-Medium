from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            res = 0
            curr_max = 0

            for j in range(i, min(len(arr), i + k)):
                curr_max = max(curr_max, arr[j])
                res = max(res, dfs(j + 1) + ((j - i + 1) * curr_max))

            cache[i] = res
            return cache[i]

        return dfs(0)


# Time:O(n*k)
# Space: O(n)

sn = Solution()
print(sn.maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
print(sn.maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
