from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        cnt = defaultdict(int)
        odd_cnt = 0

        def inorder(node):

            nonlocal odd_cnt
            if not node:
                return 0

            cnt[node.val] += 1
            odd_change = 1 if cnt[node.val] % 2 == 1 else -1
            odd_cnt += odd_change

            if not node.left and not node.right:
                res = 1 if odd_cnt <= 1 else 0
            else:
                res = inorder(node.left) + inorder(node.right)

            odd_cnt -= odd_change
            cnt[node.val] -= 1

            return res

        return inorder(root)


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

sn = Solution()
print(sn.pseudoPalindromicPaths(root))
