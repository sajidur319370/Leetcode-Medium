class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []

        for c in s:
            if c == ")":
                portion = []
                while stk[-1] != "(":
                    portion.append(stk.pop())
                stk.pop()
                stk.extend(portion)
            else:
                stk.append(c)

        return "".join(stk)


# Time:O(m * n)
# Space:O(n)

sn = Solution()
print(sn.reverseParentheses(s="(abcd)"))
print(sn.reverseParentheses(s="(u(love)i)"))
print(sn.reverseParentheses(s="(ed(et(oc))el)"))
