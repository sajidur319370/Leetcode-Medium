class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    alice += 1
                if colors[i] == "B":
                    bob += 1
        return alice > bob


# Time:O(n)
# Space:O(1)

sn = Solution()
print(sn.winnerOfGame(colors="AAABABB"))
print(sn.winnerOfGame(colors="AA"))
print(sn.winnerOfGame(colors="ABBBBBBBAAA"))
