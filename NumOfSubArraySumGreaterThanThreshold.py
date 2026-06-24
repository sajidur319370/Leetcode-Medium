from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        curSum = sum(arr[0:k-1])
        res = 0

        for i in range(N-k+1):
            curSum += arr[i+k-1]
            if (curSum/k) >= threshold:
                res+=1
            curSum -= arr[i]

        return res

# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(sn.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))