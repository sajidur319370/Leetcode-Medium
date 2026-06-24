from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        def dfs(cur,parent):
            time = 0
            for child in adj[cur]:
                if child != parent:
                    child_time = dfs(child,cur)
                    if child_time or hasApple[child]:
                        time += 2 + child_time
            return time

        return dfs(0,-1)

# Time: O(n)
# Space: O(n)

sn = Solution()
print(sn.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
print(sn.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
print(sn.minTime( n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]))