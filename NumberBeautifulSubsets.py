from typing import List, Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        group = []
        visited = set()
        for num in cnt.keys():
            if num in visited:
                continue

            g = {}
            while num - k in cnt:
                num -= k
            while num in cnt:
                g[num] = cnt[num]
                visited.add(num)
                num += k
            group.append(g)

        cache = {}

        def helper(num, g):
            if num not in g:
                return 1
            if num in cache:
                return cache[num]
            skip = helper(num + k, g)
            include = (2 ** g[num] - 1) * helper(num + 2 * k, g)
            cache[num] = skip + include
            return cache[num]

        res = 1
        for g in group:
            num = min(g.keys())
            res *= helper(num, g)

        return res - 1


# Time:O(N)
# Space:O(N)

sn = Solution()
print(sn.beautifulSubsets([11, 12, 3, 14, 5, 6, 7, 8, 9], 3))
