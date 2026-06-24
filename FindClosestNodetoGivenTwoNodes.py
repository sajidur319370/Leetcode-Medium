from collections import defaultdict, deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj =  defaultdict(list)
        for ith_node, end_node in enumerate(edges):
            adj[ith_node].append(end_node)
        def bfs(src,dist_map):
            q = deque()
            q.append([src,0])
            dist_map[src]=0
            while q:
                node , dist = q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in dist_map:
                        q.append([neighbor,dist+1])
                        dist_map[neighbor]=dist+1


        dist_map1 = defaultdict(int)
        dist_map2 = defaultdict(int)

        bfs(node1,dist_map1)
        bfs(node2,dist_map2)

        res = -1
        res_dist = float('inf')
        for i in range(len(edges)):
            if i in dist_map1 and i in dist_map2:
                dist = max(dist_map1[i],dist_map2[i])
                if res_dist > dist:
                    res_dist = dist
                    res = i
        return res

# Time: O(n)
# Space: O(n)
sn = Solution()
print(sn.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
print(sn.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))