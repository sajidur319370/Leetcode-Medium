# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return 0

            left_extra = dfs(root.left)
            right_extra = dfs(root.right)

            extra_coins = root.val - 1 + left_extra + right_extra
            self.ans += abs(extra_coins)
            return extra_coins

        dfs(root)
        return self.ans


# Time:O(N)
# Space:O(H)

root = TreeNode(3)
root.left = TreeNode(0)
root.left.left = TreeNode(0)

root2 = TreeNode(0)
root2.right = TreeNode(0)
root2.right.left = TreeNode(0)
root2.right.right = TreeNode(4)

sn = Solution()
print(sn.distributeCoins(root))
print(sn.distributeCoins(root2))
