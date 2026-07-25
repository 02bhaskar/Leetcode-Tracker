# Last updated: 7/25/2026, 4:06:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
10        if not p and not q:
11            return True
12        if not p or not q:
13            return False
14        return (p.val == q.val and 
15                self.isMirror(p.left, q.right) and 
16                self.isMirror(p.right, q.left))
17
18    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
19        if not root:
20            return True
21        return self.isMirror(root.left, root.right)