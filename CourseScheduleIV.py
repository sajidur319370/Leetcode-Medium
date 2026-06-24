from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        prereqList = defaultdict(list)
        for pre,course in prerequisites:
            prereqList[course].append(pre)

        def dfs(course, prereqMap):
            if course not in prereqMap:
                prereqMap[course] = set()
                for pre in prereqList[course]:
                    prereqMap[course] |= dfs(pre,prereqMap)
                prereqMap[course].add(course)
            return prereqMap[course]

        prereqMap = defaultdict(set)
        for course in range(numCourses):
            dfs(course,prereqMap)

        res = []
        for pre,course in queries:
            res.append(pre in prereqMap[course])

        return res

# Time:O(N^3 + Q)
# Space: O(N^2 + P)

sn =  Solution()
print(sn.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
print(sn.checkIfPrerequisite( numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
print(sn.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))