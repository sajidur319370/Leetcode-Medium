class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt_right = [0] * len(s)
        for i in reversed(range(len(s) - 1)):
            a_cnt_right[i] = a_cnt_right[i + 1]
            if s[i + 1] == "a":
                a_cnt_right[i] += 1

        b_cnt_left = 0
        res = len(s)
        for i, c in enumerate(s):
            res = min(res, a_cnt_right[i] + b_cnt_left)
            if c == "b":
                b_cnt_left += 1
        return res


# Time:O(N)
# Space:O(N)

sn = Solution()
print(sn.minimumDeletions(s="aababbab"))
print(sn.minimumDeletions(s="bbaaaaabb"))
