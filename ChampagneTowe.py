class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]

        for row in range(1, query_row + 1):
            curr_row = [0] * (row + 1)
            for glass in range(row):
                extra = prev_row[glass] - 1
                if extra > 0:
                    curr_row[glass] += 0.5 * extra
                    curr_row[glass + 1] += 0.5 * extra
            prev_row = curr_row

        return min(1, prev_row[query_glass])


# Time Complexity	O(n^2)
# Space Complexity	O(n)

sn = Solution()
print(sn.champagneTower(poured=1, query_row=1, query_glass=1))
print(sn.champagneTower(poured=2, query_row=1, query_glass=1))
print(sn.champagneTower(poured=4, query_row=2, query_glass=0))
print(sn.champagneTower(poured=100000009, query_row=33, query_glass=17))
