class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 10 ** 9 + 7
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6], [1, 3],
            [2, 4]
        ]
        dp = [1] * 10

        for _ in range(n - 1):
            next_dp = [0] * 10
            for digit in range(10):
                for j in jumps[digit]:
                    next_dp[j] = (next_dp[j] + dp[digit]) % mod
            dp = next_dp

        ans = 0
        for res in dp:
            ans = (ans + res) % mod

        return ans


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.knightDialer(1))
print(sn.knightDialer(2))
print(sn.knightDialer(3))
print(sn.knightDialer(4))
print(sn.knightDialer(3131))
