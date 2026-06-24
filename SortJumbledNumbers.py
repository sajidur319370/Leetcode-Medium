from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i, n in enumerate(nums):
            n = str(n)
            mapped_n = 0
            for c in n:
                mapped_n *= 10
                mapped_n += mapping[int(c)]
            pairs.append((mapped_n, i))

        pairs.sort()
        res = []
        for p in pairs:
            res.append(nums[p[1]])

        return res


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.sortJumbled(mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]))
