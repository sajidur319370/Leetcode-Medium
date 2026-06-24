class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i+=1
        return len(t) - j

# Time:O(S+T)
# Space:O(1)

sn = Solution()
print(sn.appendCharacters( s = "coaching", t = "coding"))
print(sn.appendCharacters( s = "abcde", t = "a"))
print(sn.appendCharacters( s = "a", t = "xyz"))