from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        cur_xor = 0
        res = 0
        for i in range(len(arr)-1):
            cur_xor = arr[i]
            for k in range(i+1, len(arr)):
                cur_xor ^= arr[k]
                if cur_xor == 0:
                    res += (k-i)

        return res


# Time:O(N^2)
# Space:O(1)

sn = Solution()
print(sn.countTriplets(arr = [2,3,1,6,7]))
print(sn.countTriplets(arr = [1,1,1,1,1]))
