class Solution:
    def minDeletions(self, s: str) -> int:
        charFreq = {}
        for char in s:
            if char not in charFreq:
                charFreq[char] = 1
            else:
                charFreq[char] += 1
        uniqueCharFreq = set()
        res = 0
        for char, count in charFreq.items():
            while count > 0 and count in uniqueCharFreq:
                count -= 1
                res += 1
            uniqueCharFreq.add(count)
        return res




# Time:O(n)
# Space:O(k)

sn = Solution()
print(sn.minDeletions(s = "aab"))
print(sn.minDeletions(s = "aaabbbcc"))
print(sn.minDeletions(s = "ceabaacb"))