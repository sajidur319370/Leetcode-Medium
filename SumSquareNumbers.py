from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l <= r:
            total = l * l + r * r
            if total < c:
                l+=1
            elif total > c:
                r-=1
            else:
                return True
        return False

# Time:O(sqrt(c))
# Space:O(1)

sn = Solution()
print(sn.judgeSquareSum(5))
print(sn.judgeSquareSum(10))
print(sn.judgeSquareSum(12))