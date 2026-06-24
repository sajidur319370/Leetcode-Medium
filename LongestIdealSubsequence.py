class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            cur = ord(c) - ord('a')
            longest = 1
            for prev in range(26):
                if abs(cur - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[cur] = max(dp[cur], longest)
        return max(dp)


# Time Complexity: O(n)
# Space Complexity: O(1)

sn = Solution()
print(sn.longestIdealString(s="acfgbd", k=2))
print(sn.longestIdealString("abcabcbb", 3))
