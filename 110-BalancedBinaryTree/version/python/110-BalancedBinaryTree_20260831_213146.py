# Last updated: 8/31/2026, 9:31:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def height(node):
10            if not node:
11                return 0
12            left = height(node.left)
13            right = height(node.right)
14            if left == -1 or right == -1:
15                return -1
16            if abs(left - right) > 1:
17                return -1
18            return max(left, right) + 1
19        return height(root) != -1