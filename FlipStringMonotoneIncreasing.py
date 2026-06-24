class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt_one = 0
        res = 0
        for d in s:
            if d == '1':
                cnt_one += 1
            else:
                res = min(res+1, cnt_one)

        return res

# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.minFlipsMonoIncr(s = "00110"))
print(sn.minFlipsMonoIncr(s = "010110"))
print(sn.minFlipsMonoIncr( s = "00011000"))