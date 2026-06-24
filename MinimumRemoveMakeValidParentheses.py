class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        temp = []
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
                temp.append(ch)

            elif ch == ')':
                if balance > 0:
                    balance -= 1
                    temp.append(ch)
            elif ch != ')':
                temp.append(ch)

        result = []
        for ch in reversed(temp):
            if ch == '(' and balance > 0:
                balance -= 1
            else:
                result.append(ch)

        return "".join(reversed(result))


# Time:O(N)
# Space:O(N)

sn = Solution()
print(sn.minRemoveToMakeValid(s="lee(t(c)o)de)"))
print(sn.minRemoveToMakeValid(s="l(e(e(t(c)o)de)"))
print(sn.minRemoveToMakeValid(s="a)b(c)d"))
print(sn.minRemoveToMakeValid(s="))(("))
