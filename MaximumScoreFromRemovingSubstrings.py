class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def max_score(pair, score):
            nonlocal s
            res = 0
            stk = []
            for c in s:
                if c == pair[1] and stk and stk[-1] == pair[0]:
                    stk.pop()
                    res += score
                else:
                    stk.append(c)
            s = "".join(stk)
            return res

        ans = 0
        pair = "ab" if x > y else "ba"
        ans += max_score(pair, max(x, y))
        ans += max_score(pair[::-1], min(x, y))
        return ans


# Time:O(N)
# Space:O(N)

sn = Solution()
print(sn.maximumGain(s="cdbcbbaaabab", x=4, y=5))
print(sn.maximumGain(s="aabbaaxybbaabb", x=5, y=4))
