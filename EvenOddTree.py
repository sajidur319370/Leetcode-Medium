from collections import deque
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev is not None and node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if prev is not None and node.val >= prev:
                        return False

                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return True


# Time:O(N)
# Space:O(w)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Raw binary tree

root = TreeNode(1)

root.left = TreeNode(10)
root.right = TreeNode(4)

root.left.left = TreeNode(3)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)

root.right.left.left = TreeNode(6)

root.right.right.right = TreeNode(2)

sn = Solution()
print(sn.isEvenOddTree(root))
