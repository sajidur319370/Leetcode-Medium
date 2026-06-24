from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        word_index = {}
        for i, word in enumerate(words):
            word_index[word] = i

        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            word = words[i]
            res = 1
            for j in range(len(word)):
                predecessor = word[:j] + word[j+1:]
                if predecessor in word_index:
                    res = max(res,1+ dfs(word_index[predecessor]))
            cache[i] = res
            return cache[i]

        for i in range(len(words)):
            dfs(i)

        return max(cache.values())

# Time:O(N * L * L)
# Space:O(N)

sn =  Solution()
print(sn.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
print(sn.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(sn.longestStrChain( words = ["abcd","dbqca"]))