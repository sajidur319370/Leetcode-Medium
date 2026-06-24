class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        left = 1
        right = 2 ** (n - 1)
        for _ in range(n - 1):

            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur == 1 else 1
        return cur


# Time:O(h)
# Space:O(1)


sn = Solution()
print(sn.kthGrammar(n=1, k=1))
print(sn.kthGrammar(n=2, k=2))
print(sn.kthGrammar(n=2, k=1))
