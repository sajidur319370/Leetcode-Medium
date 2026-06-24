class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:
            temp = s[l]
            while l <= r and s[l] == temp:
                l += 1
            while l <= r and s[r] == temp:
                r -= 1

        return r - l + 1


# Time:O(n)
# Space:O(1)
sn = Solution()
print(sn.minimumLength("ca"))
print(sn.minimumLength("bbbbbbbbbbbbbbbbbbb"))
print(sn.minimumLength(s="cabaabac"))
print(sn.minimumLength(s="aabccabba"))
