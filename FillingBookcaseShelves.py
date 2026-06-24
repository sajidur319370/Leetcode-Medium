from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}

        def helper(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = float("inf")
            maxHeight = 0
            currentWidth = shelfWidth

            for j in range(i, len(books)):
                width, height = books[j]
                if currentWidth < width:
                    break

                currentWidth -= width
                maxHeight = max(maxHeight, height)
                cache[i] = min(cache[i], helper(j + 1) + maxHeight)

            return cache[i]

        return helper(0)


# Time:O(n * w)
# Space:O(n)

sn = Solution()
print(sn.minHeightShelves(books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4))
print(sn.minHeightShelves(books=[[1, 3], [2, 4], [3, 2]], shelfWidth=6))
