from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = {i: [] for i in range(n)}

        # Build graph
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]

                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist <= r1 ** 2:
                    graph[i].append(j)
        # DFS function
        def dfs(node, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

        # Try each bomb
        res = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            res = max(res, len(visited))

        return res

# Time: O(n^3)
#Space: O(n^2)

sn = Solution()
print(sn.maximumDetonation([[1,2,3],[4,5,6]]))
print(sn.maximumDetonation([[2,1,3],[6,1,4]]))
print(sn.maximumDetonation( [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))
