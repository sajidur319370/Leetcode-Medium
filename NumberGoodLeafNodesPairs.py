from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.pairs = 0

        def dfs(node):

            if not node:
                return defaultdict(int)

            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.pairs += left_dist[d1] * right_dist[d2]

            all_dist = defaultdict(int)
            for d1 in left_dist:
                if d1 + 1 <= distance:
                    all_dist[d1 + 1] += left_dist[d1]
            for d2 in right_dist:
                if d2 + 1 <= distance:
                    all_dist[d2 + 1] += right_dist[d2]

            return all_dist

        dfs(root)
        return self.pairs


# Time:O(N * d^2)
# Space:O(N * d^2)

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left.left = TreeNode(8)
root.right.right.right = TreeNode(9)
sn = Solution()
print(sn.countPairs(root, 3))
