from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = bank[0].count("1")
        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                result += (prev * curr)
                prev = curr

        return result


# Time:O(m * n)
# Space:O(1)

sn = Solution()
print(sn.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(sn.numberOfBeams(bank=["000", "111", "000"]))
