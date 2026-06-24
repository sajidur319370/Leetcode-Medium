from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [ [0]* n for i in range(n) ]
        top = 0
        bottom = n- 1
        left = 0
        right = n-1
        num = 1
        while top <= bottom and left <= right:

            # left → right
            for j in range(left, right + 1):
                result[top][j] = num
                num += 1
            top += 1

            # top → bottom
            for i in range(top, bottom + 1):
                result[i][right] = num
                num += 1
            right -= 1

            # right → left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result[bottom][j] = num
                    num += 1
                bottom -= 1

            # bottom → top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result[i][left] = num
                    num += 1
                left += 1

        return result

# Time: O(n * n)
# Space:O(n * n)

sn = Solution()
print(sn.generateMatrix(1))
print(sn.generateMatrix(2))
print(sn.generateMatrix(3))
print(sn.generateMatrix(4))