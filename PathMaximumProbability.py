import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            src,dst = edges[i]
            adjList[src].append([dst,succProb[i]])
            adjList[dst].append([src,succProb[i]])

        pq = [(-1,start_node)]
        visited = set()
        while pq:
            probability,node = heapq.heappop(pq)
            visited.add(node)

            if node == end_node:
                return probability * -1

            for neighbor,edgeProbability in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(pq,(probability* edgeProbability,neighbor))

        return  0

# Time	O(E log V)
# Space	O(E + V)



sn = Solution()
print(sn.maxProbability( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(sn.maxProbability( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))
