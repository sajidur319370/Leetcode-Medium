from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            cnt = 1
            while stack and stack[-1][0] > arr[i]:
                elem, c = stack.pop()
                cnt += c
            left[i] = cnt
            stack.append((arr[i], cnt))

        stack = []
        for i in range(n - 1, -1, -1):
            cnt = 1
            while stack and stack[-1][0] >= arr[i]:
                elem, c = stack.pop()
                cnt += c
            right[i] = cnt
            stack.append((arr[i], cnt))

        res = 0
        for i in range(n):
            res = (res + arr[i] * left[i] * right[i]) % mod

        return res


# Time: O(n)
# Space: O(n)

sn = Solution()
print(sn.sumSubarrayMins([3, 1, 2, 4]))
print(sn.sumSubarrayMins([11, 81, 94, 43, 3]))
