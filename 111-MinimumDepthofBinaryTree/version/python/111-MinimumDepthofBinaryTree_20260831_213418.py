# Last updated: 8/31/2026, 9:34:18 PM
1class Solution:
2    def minDepth(self, root):
3        if root is None:
4            return 0
5
6        if root.left is None:
7            return 1 + self.minDepth(root.right)
8
9        if root.right is None:
10            return 1 + self.minDepth(root.left)
11
12        return 1 + min(
13            self.minDepth(root.left),
14            self.minDepth(root.right)
15        )