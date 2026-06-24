class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10 ** 9 + 7
        cache = {}

        def count_ways(dice_left, remaining_target):
            if dice_left == 0:
                return 1 if remaining_target == 0 else 0

            if (dice_left, remaining_target) in cache:
                return cache[(dice_left, remaining_target)]

            res = 0

            for face in range(1, k + 1):
                res = (res + count_ways(dice_left - 1, remaining_target - face)) % mod

            cache[(dice_left, remaining_target)] = res
            return res

        return count_ways(n, target)


# Time:O(n * t * k)
# Space:O(n * t )

sn = Solution()
print(sn.numRollsToTarget(n=1, k=6, target=3))
print(sn.numRollsToTarget(n=2, k=6, target=7))
print(sn.numRollsToTarget(n=30, k=30, target=500))
