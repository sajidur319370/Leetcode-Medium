from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        bucket = defaultdict(list)
        res = []
        for c, val in cnt.items():
            bucket[val].append(c)

        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                res.append(c * i)

        return "".join(res)


# Time:O(n)
# Space:O(n)
sn = Solution()
print(sn.frequencySort(s="tree"))
print(sn.frequencySort(s="cccaaa"))
print(sn.frequencySort(s="Aabb"))
