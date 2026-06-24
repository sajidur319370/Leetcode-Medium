from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Option 1: treat s[i] as extra
            dp[i] = 1 + dp[i + 1]

            # Option 2: match dictionary words
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[0]

# Time: O(n^3)
# Space: O(n)

sn = Solution()
print(sn.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
print(sn.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))
