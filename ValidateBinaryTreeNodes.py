from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        has_parent = set(leftChild + rightChild)
        has_parent.discard(-1)

        if len(has_parent) == n:
            return False

        root = -1
        for i in range(n):
            if i not in has_parent:
                root = i

        visited = set()

        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visited) == n


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(sn.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(sn.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))
