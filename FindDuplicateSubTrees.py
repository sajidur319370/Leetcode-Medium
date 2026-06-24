from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        res = []
        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), dfs(node.left),dfs(node.right)])
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        dfs(root)
        return res

# Time: O(N * N)
# Space: O(N * N)

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(3)

sn = Solution()
print(sn.findDuplicateSubtrees(root))