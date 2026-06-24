from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for parent, child, is_left in descriptions:
            if parent not in children:
                return nodes[parent]


# Time:O(n)
# Space:O(n)

sn = Solution()
print(sn.createBinaryTree(descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]))
