class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # Traverse from right to left (excluding first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                # odd -> +1 then /2
                steps += 2
                carry = 1
            else:
                # even -> /2
                steps += 1

        # If carry remains, one extra step needed
        return steps + carry


# Time: O(n)
# Space: O(1)


sn = Solution()
print(sn.numSteps(s="1101"))
print(sn.numSteps(s="1101000100"))
print(sn.numSteps(s="10"))
