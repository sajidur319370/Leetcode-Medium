class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cost = 0
        max_len = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# Time: O(n)
# Space: O(1)

sn = Solution()
print(sn.equalSubstring(s="abcd", t="bcdf", maxCost=3))
print(sn.equalSubstring(s="abcd", t="cdef", maxCost=3))
print(sn.equalSubstring(s="abcd", t="acde", maxCost=0))
