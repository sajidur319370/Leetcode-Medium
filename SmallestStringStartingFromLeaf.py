from typing import Optional


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node, cur):
            if not node:
                return
            cur = chr(ord('a') + node.val) + cur
            if node.left and node.right:
                return min(helper(node.left, cur), helper(node.right, cur))

            if node.left:
                return helper(node.left, cur)
            if node.right:
                return helper(node.right, cur)
            return cur

        return helper(root, "")


# Time	O(N²)
# Space	O(N)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Input Tree

#         0
#       /   \
#      1     2
#     / \   / \
#    3   4 3   4

root = TreeNode(0)

root.left = TreeNode(1)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

sn = Solution()
print(sn.smallestFromLeaf(root))
