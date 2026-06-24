# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


# Time:O(N)
# Space:O(1)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(3)
root1.left.left.left.left = TreeNode(3)

sn = Solution()
print(sn.removeLeafNodes(root1, 3))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(2)
root2.right.left = TreeNode(2)
root2.right.right = TreeNode(4)

sn = Solution()
print(sn.removeLeafNodes(root2, 3))
